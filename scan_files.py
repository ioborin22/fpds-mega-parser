import os
import json
import mysql.connector
import re  # Для проверки формата имени файла
from pathlib import Path
from datetime import datetime
from fpds.config import DB_CONFIG  # Используем конфиг для подключения к MySQL

# Путь к папке с файлами
DATA_DIR = Path("/Volumes/Storage01/data")

# Статусы файлов
STATUS_FILE_MISSING = "file_missing"
STATUS_FILE_FOUND = "file_found"


def get_db_connection():
    """Подключение к базе данных."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(f"⚠️ Ошибка подключения к БД: {e}")
        return None


def file_exists_in_db(cursor, signed_date):
    """Проверяет, есть ли запись в БД для данной даты."""
    query = """
    SELECT COUNT(*) FROM file_processing_status WHERE signed_date = %s;
    """
    cursor.execute(query, (signed_date,))
    return cursor.fetchone()[0] > 0


def scan_and_insert_files():
    """Сканирует файлы в папке и добавляет их в БД, если они отсутствуют."""
    conn = get_db_connection()
    if not conn:
        return
    cursor = conn.cursor()

    for year_dir in sorted(DATA_DIR.iterdir()):
        if year_dir.is_dir() and year_dir.name.isdigit():  # Проверяем, что это директория с годом
            for json_file in sorted(year_dir.glob("*.json")):
                file_name = json_file.name  # Имя файла, включая .json

                # Проверяем, соответствует ли имя формату MM_DD.json
                if not re.match(r"^\d{2}_\d{2}\.json$", file_name):
                    print(
                        f"⚠️ Пропускаем файл с некорректным именем: {file_name}")
                    continue  # Пропускаем файлы с неподходящим именем

                # Получаем год и имя файла без .json
                year, month_day = year_dir.name, json_file.stem
                month, day = month_day.split("_")
                signed_date = f"{year}-{month}-{day}"

                if file_exists_in_db(cursor, signed_date):
                    print(f"⏭ Пропускаем, запись уже есть: {signed_date}")
                    continue

                # Получаем размер файла в байтах
                file_size = json_file.stat().st_size

                # Считаем количество записей в файле
                try:
                    with open(json_file, "r") as f:
                        records = json.load(f)
                        record_count = len(records) if isinstance(
                            records, list) else 0
                except Exception as e:
                    print(f"❌ Ошибка чтения {json_file}: {e}")
                    continue

                # Добавляем запись в БД
                query = """
                INSERT INTO file_processing_status (signed_date, record_count, file_size_bytes, file_path, status)
                VALUES (%s, %s, %s, %s, %s);
                """
                cursor.execute(query, (signed_date, record_count,
                               file_size, str(json_file), STATUS_FILE_FOUND))
                conn.commit()
                print(
                    f"✅ Добавлен файл {json_file} ({record_count} записей, {file_size} байт)")

    cursor.close()
    conn.close()
    print("🎉 Завершено сканирование файлов!")


if __name__ == "__main__":
    scan_and_insert_files()
