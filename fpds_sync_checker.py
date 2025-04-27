import clickhouse_connect
import mysql.connector
from fpds.config import DB_CONFIG
import sys
import subprocess
import shutil
from pathlib import Path
from clickhouse_driver import Client
from datetime import datetime

client = Client(
            host='localhost',
            port=9000,
            user='default',
            password='',
            database='fpds_clickhouse'
        )

def get_clickhouse_data():
    """
    Запрашивает данные из ClickHouse, группируя по partition_date.
    Форматирует дату как 'YYYY-MM-DD'.
    """
    client = clickhouse_connect.get_client(host="localhost", port=8123)
    query = """
        SELECT 
            partition_date, 
            COUNT(*) as count
        FROM fpds_clickhouse.raw_contracts
        GROUP BY partition_date
        ORDER BY partition_date
    """
    result = client.query(query)
    data = {}
    for row in result.result_rows:
        partition_date, count = row
        # partition_date уже в формате datetime.date
        date_str = partition_date.strftime("%Y-%m-%d")
        data[date_str] = count
    return data


def get_mysql_data():
    """
    Запрашивает данные из MySQL из таблицы signed_date_records,
    группируя по дате и суммируя поле fpds_records.
    """
    db_conn = mysql.connector.connect(**DB_CONFIG)
    cursor = db_conn.cursor()
    query = """
        SELECT DATE(signed_date) as date, SUM(fpds_records) as count
        FROM signed_date_records
        WHERE fpds_respond IS NULL
        GROUP BY date
    """
    cursor.execute(query)
    data = {}
    for row in cursor.fetchall():
        date_val, count = row
        date_str = date_val.strftime("%Y-%m-%d")
        data[date_str] = count
    cursor.close()
    db_conn.close()
    return data


def compare_data():
    """
    Сравнивает данные из ClickHouse и MySQL.
    Возвращает список кортежей (дата, count_clickhouse, count_mysql) для дат,
    где разница не равна 0.
    """
    ch_data = get_clickhouse_data()
    mysql_data = get_mysql_data()
    all_dates = set(ch_data.keys()).union(mysql_data.keys())
    issues = []
    for date in sorted(all_dates):
        ch_count = ch_data.get(date, 0)
        mysql_count = mysql_data.get(date, 0)
        if ch_count != mysql_count:
            issues.append((date, ch_count, mysql_count))
    return issues


def main():
    issues = compare_data()
    if issues:
        date, ch_count, mysql_count = issues[0]
        diff = ch_count - mysql_count
        print(f"🚨 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Найдено расхождение: Дата: {date}, ClickHouse: {ch_count}, FPDS: {mysql_count}, Разница: {diff}")

        # ✅ Шаг 1: DROP ClickHouse
        print(f"🗑  [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Удаляем партицию за дату {date}...")
        try:
            drop_partition_sql = f"ALTER TABLE raw_contracts DROP PARTITION '{date}'"
            client.execute(drop_partition_sql)
            print(f"🔥 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Партиция успешно удалена.")
        except Exception as e:
            print(f"⚠️ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ошибка удаления партиции: {e}")

        # ✅ Шаг 2: Скачиваем JSON для этой даты
        date_slash = date.replace("-", "/")  # преобразуем в формат YYYY/MM/DD
        subprocess.run(["fpds", "get", date_slash])

        # ✅ Шаг 3: Вставка напрямую
        subprocess.run(["python", "insert_json_clickhouse_direct.py", date])

        # ✅ Шаг 4: Перемещаем файл
        year = date[:4]
        month_day = date[5:7] + "_" + date[8:10]

        source_file = Path(rf"C:\Users\iobor\Projects\fpds\data\{year}\{month_day}.json")
        destination_file = Path(rf"D:\data\{year}\{month_day}.json")

        try:
            if source_file.exists():
                destination_file.parent.mkdir(parents=True, exist_ok=True)
                print(f"📂 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Перемещаем файл {source_file} в {destination_file}...")
                shutil.move(str(source_file), str(destination_file))
                print(f"▶️ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Файл успешно перемещён.")
            else:
                print(f"⚠️ Файл {source_file} не найден, пропуск перемещения.")
        except Exception as e:
            print(f"⚠️ Ошибка при перемещении файла: {e}")



if __name__ == "__main__":
    main()
