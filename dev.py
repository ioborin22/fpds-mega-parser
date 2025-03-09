import asyncio
import json
import mysql.connector
import click
import os
import time
import sys
import gc
from datetime import datetime, timedelta
from pathlib import Path
import clickhouse_connect

from fpds.cli.parts.utils import process_booleans, log_missing_keys
from fpds.cli.parts.contract_parser import extract_contract_data
from fpds.cli.parts.columns import columns
from fpds.cli.parts.bool_fields import bool_fields
from fpds import fpdsRequest
from fpds.config import DB_CONFIG

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
    return datetime(2004, 12, 31), 'completed'  # Начинаем с 2005-01-01


def check_existing_file(date):
    year, month, day = date.split("/")
    file_path = DATA_DIR / year / f"{month}_{day}.json"
    return file_path if file_path.exists() else None


def fetch_fpds_data(date):
    formatted_date = f"LAST_MOD_DATE=[{date},{date}]"
    params = dict([formatted_date.split("=")])
    request = fpdsRequest(**params, cli_run=True)
    click.echo("🌐 Запрашиваем FPDS данные...")
    return asyncio.run(request.data())


def save_data_to_file(data, file_path):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as outfile:
        json.dump(data, outfile)
    click.echo(f"📄 Сохранено {len(data)} записей в JSON: {file_path}")


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
    client = clickhouse_connect.get_client(
        host="localhost", port=8123, database="fpds_clickhouse")
    last_parsed_date, last_status = get_last_parsed_date()

    if date.lower() == "all":
        next_parsing_date = (last_parsed_date + timedelta(days=1)
                             ) if last_status == "completed" else last_parsed_date
        date = next_parsing_date.strftime("%Y/%m/%d")
        click.echo(f"🚀 Начинаем парсинг с {date}")

    file_path = check_existing_file(date)
    if last_status == "failed" and file_path:
        click.echo("🔄 Повторная вставка данных в ClickHouse")
        process_data_and_insert(file_path, client)
        log_parsing_result(date, str(file_path), "completed", update=True)
        return

    if not file_path:
        data = fetch_fpds_data(date)
        if not data:
            click.echo(f"⚠️ Нет данных за {date}, пропускаем.")
            return

        year, month, day = date.split("/")
        file_path = DATA_DIR / year / f"{month}_{day}.json"
        save_data_to_file(data, file_path)

    process_data_and_insert(file_path, client)
    log_parsing_result(date, str(file_path), "completed", update=True)
    os.remove(file_path)
    click.echo(f"🗑 Удалён JSON файл: {file_path}")
