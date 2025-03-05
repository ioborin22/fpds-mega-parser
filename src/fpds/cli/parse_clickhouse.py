import asyncio
import json
import mysql.connector
import click
import os
import time
import sys
# Импортируем список колонок для ClickHouse
from fpds.cli.parts.columns import columns
# Импортируем функцию `convert_bool`, которая конвертирует булевы значения ("true"/"false") в 1/0
from fpds.cli.parts.utils import convert_bool
# Импортируем список булевых полей, которые должны быть обработаны как 1/0
from fpds.cli.parts.bool_fields import bool_fields
# Импортируем функцию парсинга контракта
from fpds.cli.parts.contract_parser import extract_contract_data
from fpds.cli.parts.utils import log_missing_keys
from fpds.cli.parts.utils import process_booleans

from datetime import datetime, timedelta
from itertools import chain
from pathlib import Path
from click import UsageError

from fpds import fpdsRequest
from fpds.utilities import validate_kwarg
from fpds.config import DB_CONFIG


def get_db_connection():
    """Creates and returns a database connection"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as e:
        click.echo(f"⚠️ Database connection error: {e}")
        return None


def log_parsing_result(parsed_date, file_path, status, update=False):
    """Logs the parsing result in the database"""
    conn = get_db_connection()
    if conn is None:
        click.echo("⚠️ Unable to connect to the database")
        return False

    cursor = conn.cursor()

    # Colored statuses
    status_colors = {
        "completed": "green",
        "pending": "yellow",
        "failed": "red"
    }

    colored_status = click.style(status, fg=status_colors.get(status, "white"))

    if update:
        cursor.execute(
            "UPDATE parser_stage SET status = %s, updated_at = NOW() WHERE parsed_date = %s",
            (status, parsed_date)
        )
        conn.commit()
        click.echo(
            f"📝 Parsing status updated for {parsed_date}: {colored_status}")
    else:
        cursor.execute(
            "SELECT 1 FROM parser_stage WHERE parsed_date = %s", (parsed_date,))
        exists = cursor.fetchone()

        if exists:
            click.echo(
                f"⚠️ Data for {parsed_date} already exists in the database. Skipping download.")
            conn.close()
            return False
        else:
            cursor.execute(
                "INSERT INTO parser_stage (parsed_date, file_path, status, created_at, updated_at) "
                "VALUES (%s, %s, %s, NOW(), NOW())",
                (parsed_date, file_path, status)
            )
            conn.commit()
            click.echo(
                f"✅ Data for {parsed_date} successfully added to the database with status: {colored_status}")

    conn.close()
    return True


@click.command()
@click.argument("date")
def parse_clickhouse(date):
    """
    Парсит FPDS Atom feed и сохраняет JSON-контракты в ClickHouse с разбиением на чанки.

    Использование:
        $ fpds parse clickhouse all
    """
    import clickhouse_connect

    # ✅ Устанавливаем размер чанка
    BATCH_SIZE = 1000
    batch = []
    total_inserted = 0

    client = clickhouse_connect.get_client(
        host="localhost", port=8123, database="fpds_clickhouse"
    )

    conn = get_db_connection()
    if conn is None:
        click.echo("⚠️ Не удалось подключиться к MySQL.")
        return

    cursor = conn.cursor()

    if date.lower() == "all":
        click.echo("🔍 Определяем последнюю обработанную дату...")

        cursor.execute("""
            SELECT MAX(parsed_date) FROM parser_stage WHERE status = 'completed'
        """)
        last_parsed_date = cursor.fetchone()[0]

        if last_parsed_date is None:
            click.echo("⚠️ Нет завершённых записей. Начинаем с 1957-09-30.")
            last_parsed_date = datetime(1957, 9, 30)  # Старт с 1957 года
        else:
            last_parsed_date = datetime.strptime(
                str(last_parsed_date), "%Y-%m-%d")

        next_parsing_date = last_parsed_date + timedelta(days=1)
        date = next_parsing_date.strftime("%Y/%m/%d")

        click.echo(f"🚀 Начинаем парсинг с {date}")

    while True:
        year, month, day = date.split("/")
        DATA_FILE = Path(os.getenv(
            "DATA_DIR", "/Users/iliaoborin/fpds/data/")) / str(year) / f"{month}_{day}.json"

        if not log_parsing_result(date, str(DATA_FILE), "completed"):
            next_parsing_date = datetime.strptime(
                date, "%Y/%m/%d") + timedelta(days=1)
            date = next_parsing_date.strftime("%Y/%m/%d")
            year, month, day = date.split("/")
            click.echo(
                f"🔄 Данные за {date} уже есть. Пробуем следующую дату...")
            continue

        break

    formatted_date = f"SIGNED_DATE=[{date},{date}]"
    params = [formatted_date.split("=")]

    if not params:
        raise UsageError("Пожалуйста, укажите хотя бы один параметр")

    params_kwargs = dict(params)
    click.echo(f"🔍 Параметры для FPDS: {params_kwargs}")

    request = fpdsRequest(**params_kwargs, cli_run=True)
    click.echo("🌐 Получаем записи FPDS...")

    try:
        data = asyncio.run(request.data())
        records = list(chain.from_iterable(data))

        DATA_DIR = Path(
            os.getenv("DATA_DIR", "/Users/iliaoborin/fpds/data/")) / str(year)
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        with open(DATA_FILE, "w") as outfile:
            json.dump(records, outfile)

        click.echo(f"📄 Сохранено {len(records)} записей в JSON: {DATA_FILE}")

        if not records:
            click.echo(
                f"⚠️ Нет данных за {date}. Пропускаем загрузку в ClickHouse.")
            os.remove(DATA_FILE)
            return

        # ✅ Загружаем JSON в ClickHouse чанками (по 5000 записей)
        for i in range(0, len(records), BATCH_SIZE):
            batch = []

            for contract in records[i: i + BATCH_SIZE]:
                signed_date = (
                    contract.get("content__award__relevantContractDates__signedDate")
                    or contract.get("content__IDV__relevantContractDates__signedDate")
                    or contract.get("content__OtherTransactionAward__contractDetail__relevantContractDates__signedDate")
                    or contract.get("content__OtherTransactionIDV__contractDetail__relevantContractDates__signedDate")
                )

                partition_year = datetime.strptime(
                    signed_date, "%Y-%m-%d %H:%M:%S").year if signed_date else None

                # 🔄 Конвертируем булевые значения перед сохранением
                contract = process_booleans(contract, bool_fields)

                # 📦 Извлекаем и структурируем данные контракта перед вставкой в ClickHouse
                contract_data = extract_contract_data(contract, partition_year)

                # 🔍 Логируем пропущенные переменные
                log_missing_keys(contract, columns, DATA_FILE)

                batch.append(contract_data)



            # Вставка чанка в ClickHouse
            if batch:
                client.insert("raw_contracts", batch, column_names=columns)
                total_inserted += len(batch)
                sys.stdout.write(
                    f"\r✅ Загружено {total_inserted} контрактов в ClickHouse")
                sys.stdout.flush()

                # Очищаем batch для следующей итерации
                batch.clear()
                time.sleep(1)

        log_parsing_result(date, str(DATA_FILE), "completed", update=True)

    except Exception as e:
        log_parsing_result(date, str(DATA_FILE), "failed", update=True)
        click.echo(f"❌ Ошибка при парсинге: {e}")

    conn.close()
