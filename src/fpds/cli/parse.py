import asyncio
import json
import mysql.connector
from itertools import chain
from pathlib import Path

import click
from click import UsageError

from fpds import fpdsRequest
from fpds.utilities import validate_kwarg

# Конфигурация для подключения к MySQL
DB_CONFIG = {
    "host": "localhost",
    "port": 8889,  # MySQL на MAMP (phpMyAdmin)
    "user": "root",
    "password": "root",
    "database": "gov",
}

def get_db_connection():
    """Создание и возврат подключения к базе данных"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as e:
        click.echo(f"⚠️ Ошибка подключения к базе данных: {e}")
        return None

def log_parsing_result(date, status):
    """Логирование статуса парсинга в базе данных"""
    conn = get_db_connection()
    if conn is None:
        click.echo("⚠️ Не удалось подключиться к базе данных")
        return False
    
    cursor = conn.cursor()
    
    # Проверяем, существует ли запись
    cursor.execute("SELECT 1 FROM fpds_parser WHERE first_run_at = %s", (date,))
    exists = cursor.fetchone()

    if exists:
        click.echo(f"⚠️ Данные за {date} уже добавлены в базу данных. Пропускаем загрузку.")
        conn.close()
        return False
    else:
        cursor.execute(
            "INSERT INTO fpds_parser (first_run_at, status, last_run_at) VALUES (%s, %s, NOW())",
            (date, status)
        )
        conn.commit()
        click.echo(f"✅ Данные за {date} успешно добавлены в базу данных")
    
    conn.close()
    return True

@click.command()
@click.option("-o", "--output", required=False, help="Output directory")
@click.argument("date")
def parse(date, output):
    """
    Parsing command for the FPDS Atom feed with date input

    \b
    Usage:
        $ fpds parse YYYY/MM/DD [OPTIONS]
    """

    # Проверяем, существует ли запись в базе перед скачиванием данных
    if not log_parsing_result(date, "pending"):
        return

    formatted_date = f"SIGNED_DATE=[{date},{date}]"
    params = [formatted_date.split("=")]

    if not params:
        raise UsageError("Please provide at least one parameter")

    for _param in params:  # _param is a tuple
        name, value = _param
        _param[1] = validate_kwarg(kwarg=name, string=value)

    params_kwargs = dict(params)
    click.echo(f"Params to be used for FPDS search: {params_kwargs}")

    request = fpdsRequest(**params_kwargs, cli_run=True)
    click.echo("Retrieving FPDS records from ATOM feed...")

    try:
        data = asyncio.run(request.data())
        records = list(chain.from_iterable(data))

        # Разбиваем дату на компоненты
        year, month, day = date.split("/")
        DATA_DIR = Path("/Users/iliaoborin/fpds/data") / year
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        
        # Название файла в формате MM_DD.json
        DATA_FILE = DATA_DIR / f"{month}_{day}.json"
        with open(DATA_FILE, "w") as outfile:
            json.dump(records, outfile)

        log_parsing_result(date, "completed")
        click.echo(f"{len(records)} records have been saved as JSON at: {DATA_FILE}")
    except Exception as e:
        log_parsing_result(date, "error")
        click.echo(f"Error occurred while parsing: {e}")
