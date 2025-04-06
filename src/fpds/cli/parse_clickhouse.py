import asyncio
import json
import mysql.connector
import click
import time
import gc
from datetime import datetime, timedelta
from pathlib import Path
from itertools import chain

from fpds.cli.parts.utils import process_booleans, log_missing_keys
from fpds.cli.parts.contract_parser import extract_contract_data
from fpds.cli.parts.columns import columns
from fpds.cli.parts.bool_fields import bool_fields
from fpds import fpdsRequest
from fpds.config import DB_CONFIG

import warnings
warnings.filterwarnings("ignore")

BATCH_SIZE = 1000
DATA_DIR = Path("/Users/iliaoborin/fpds/data/")


def get_db_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        click.echo(f"⚠️ Database connection error: {e}")
        return None


def get_last_parsed_date():
    conn = get_db_connection()
    if not conn:
        return None, None

    cursor = conn.cursor()
    cursor.execute(
        "SELECT parsed_date, status FROM parser_stage ORDER BY parsed_date DESC LIMIT 1")
    last_parsed_record = cursor.fetchone()
    conn.close()

    if last_parsed_record:
        return datetime.strptime(str(last_parsed_record[0]), "%Y-%m-%d"), last_parsed_record[1]
    return datetime(1957, 9, 30), 'completed'  # Начинаем с 1957-09-30


def check_existing_file(date):
    year, month, day = date.split("/")
    file_path = DATA_DIR / year / f"{month}_{day}.json"

    click.echo(f"🔍 Проверяем путь: {file_path}")  # Логируем путь

    if not file_path.exists():
        click.echo("❌ Файл отсутствует.")
        return None

    if file_path.stat().st_size == 0:
        click.echo("⚠️ Файл пуст.")
        return None

    try:
        with open(file_path, "r") as f:
            json.load(f)  # Проверяем, корректный ли JSON
        click.echo("✅ Файл содержит данные.")
        return file_path
    except json.JSONDecodeError:
        click.echo("❌ Файл битый (невалидный JSON).")
        return None


def fetch_fpds_data(date):
    formatted_date = f"SIGNED_DATE=[{date},{date}]"
    params = dict([formatted_date.split("=")])
    request = fpdsRequest(**params, cli_run=True)
    print("🌐 Запрашиваем FPDS данные...")

    data = asyncio.run(request.data())  # data - список списков
    return list(chain.from_iterable(data))  # Делаем плоский список


def save_data_to_file(data, file_path):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as outfile:
        json.dump(data, outfile, indent=4)  # Добавим отступы для читаемости
    print(f"📄 Сохранено {len(data)} записей в JSON: {file_path}")


def generate_file_path(date):
    """Создаёт путь к файлу JSON на основе даты."""
    year, month, day = date.split("/")
    return DATA_DIR / year / f"{month}_{day}.json"

def log_parsing_result(parsed_date, file_path, status, update=False):
    conn = get_db_connection()
    if not conn:
        return False

    cursor = conn.cursor()
    if update:
        cursor.execute(
            "UPDATE parser_stage SET status = %s, updated_at = NOW() WHERE parsed_date = %s",
            (status, parsed_date)
        )
    else:
        cursor.execute(
            "INSERT INTO parser_stage (parsed_date, file_path, status, created_at, updated_at) "
            "VALUES (%s, %s, %s, NOW(), NOW())",
            (parsed_date, file_path, status)
        )
    conn.commit()
    conn.close()
    return True


def insert_into_clickhouse(client, batch):
    asyncio.run(asyncio.to_thread(client.insert,
                "raw_contracts", batch, column_names=columns))


def process_data_and_insert(file_path, client):
    with open(file_path, "r") as f:
        records = json.load(f)

    total_inserted = 0
    for i in range(0, len(records), BATCH_SIZE):
        batch = []
        for contract in records[i:i + BATCH_SIZE]:
            partition_year = datetime.strptime(contract.get(
                "signed_date", "2000-01-01"), "%Y-%m-%d").year
            contract = process_booleans(contract, bool_fields)
            contract_data = extract_contract_data(contract, partition_year)
            log_missing_keys(contract, columns, file_path)
            batch.append(contract_data)

        if batch:
            insert_into_clickhouse(client, batch)
            total_inserted += len(batch)
            click.echo(f"✅ Загружено {total_inserted} контрактов в ClickHouse")
            gc.collect()
            time.sleep(5)


@click.command()
@click.argument("date")
def parse_clickhouse(date):
    """Основной процесс парсинга: скачивание, обработка и вставка в ClickHouse."""

    last_parsed_date, last_status = get_last_parsed_date()

    # Выводим текущий статус
    click.echo(
        f"📅 Последняя обработанная дата: {last_parsed_date.strftime('%Y-%m-%d')}, Статус: {last_status}")

    if last_status == "completed":
        # Создаём новую запись для следующей даты со статусом 'pending'
        next_parsing_date = last_parsed_date + timedelta(days=1)
        click.echo(
            f"📝 Добавляем новую дату в БД: {next_parsing_date.strftime('%Y-%m-%d')} со статусом 'pending'")
        file_path = generate_file_path(next_parsing_date.strftime('%Y/%m/%d'))
        log_parsing_result(next_parsing_date.strftime(
            '%Y-%m-%d'), str(file_path), "pending")

    elif last_status == "pending":
        # Начинаем скачивание данных
        file_path = generate_file_path(last_parsed_date.strftime('%Y/%m/%d'))
        click.echo(
            f"🌐 Начинаем скачивание данных для {last_parsed_date.strftime('%Y-%m-%d')}")

        # Обновляем статус на 'running'
        log_parsing_result(last_parsed_date.strftime(
            '%Y-%m-%d'), str(file_path), "running", update=True)

        data = fetch_fpds_data(last_parsed_date.strftime('%Y/%m/%d'))

        if not data:
            click.echo(
                f"⚠️ Нет данных за {last_parsed_date.strftime('%Y-%m-%d')}, ставим 'completed'")
            log_parsing_result(last_parsed_date.strftime(
                '%Y-%m-%d'), str(file_path), "completed", update=True)
            return
        
        # ✅ Генерируем путь к файлу перед сохранением
        file_path = generate_file_path(last_parsed_date.strftime('%Y/%m/%d'))

        save_data_to_file(data, file_path)
        click.echo(f"📄 Данные сохранены в {file_path}")

    elif last_status == "running":
        click.echo("🔄 Парсинг уже выполняется, проверяем файл...")

        # Проверяем, существует ли файл и содержит ли данные
        file_path = check_existing_file(last_parsed_date.strftime('%Y/%m/%d'))

        if file_path:
            click.echo(
                f"✅ Файл найден: {file_path}, продолжаем обработку и вставку в ClickHouse")

            # Обновляем статус на 'completed'
            log_parsing_result(last_parsed_date.strftime(
                '%Y-%m-%d'), str(file_path), "completed", update=True)
            click.echo("✅ Данные успешно загружены в ClickHouse, статус 'completed'")

        else:
            click.echo(f"❌ Ошибка на статусе 'running', меняем статус на 'failed'.")
            log_parsing_result(last_parsed_date.strftime('%Y-%m-%d'), "", "failed", update=True)

    elif last_status == "failed":
        # Повторная попытка парсинга
        click.echo(
            f"❌ Ошибка при предыдущем парсинге {last_parsed_date.strftime('%Y-%m-%d')}, пробуем снова.")
        file_path = check_existing_file(last_parsed_date.strftime('%Y/%m/%d'))

        if file_path:
            click.echo(
                f"✅ Файл найден: {file_path}, пробуем снова загрузить в ClickHouse")
        else:
            click.echo("⚠️ Файл не найден, повторное скачивание.")
            data = fetch_fpds_data(last_parsed_date.strftime('%Y/%m/%d'))

            if not data:
                click.echo(
                    "❌ Повторное скачивание не дало результатов, остаётся 'failed'.")
                return

            # ✅ Генерируем путь к файлу перед сохранением 
            file_path = generate_file_path(last_parsed_date.strftime('%Y/%m/%d'))
            save_data_to_file(data, file_path)


        # Обновляем статус на 'completed'
        log_parsing_result(last_parsed_date.strftime(
            '%Y-%m-%d'), str(file_path), "completed", update=True)
        click.echo("✅ Данные успешно загружены в ClickHouse, статус 'completed'")


@click.command(name="get")
@click.argument("date")
@click.option("-o", "--output", required=False, help="Output directory")
def get_fpds(date, output):
    """
    Download FPDS data for a specific date and save as JSON.

    Example:
        fpds get 2004/07/14
    """
    try:
        year, month, day = date.split("/")
    except ValueError:
        click.echo(
            f"⚠️ Invalid date format: {date}. Expected format: YYYY/MM/DD")
        return

    data_dir = Path(output) if output else Path("/Users/iliaoborin/fpds/data/")
    data_file = data_dir / year / f"{month}_{day}.json"

    formatted_date = f"SIGNED_DATE=[{date},{date}]"
    params = dict([formatted_date.split("=")])

    click.echo(f"🌐 Downloading FPDS data for {date}...")

    request = fpdsRequest(**params, cli_run=True)

    try:
        data = asyncio.run(request.data())
        records = list(chain.from_iterable(data))

        # Создаем папку, если не существует
        data_file.parent.mkdir(parents=True, exist_ok=True)

        # Сохраняем в JSON
        with open(data_file, "w") as outfile:
            json.dump(records, outfile, indent=4)

        click.echo(f"✅ Saved {len(records)} records to {data_file}")

        if not records:
            click.echo("⚠️ No records found. The file is empty.")

    except Exception as e:
        click.echo(f"❌ Error occurred: {e}")
