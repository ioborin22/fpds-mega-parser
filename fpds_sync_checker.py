import clickhouse_connect
import mysql.connector
from fpds.config import DB_CONFIG
import sys


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
    группируя по дате и суммируя поле records.
    """
    db_conn = mysql.connector.connect(**DB_CONFIG)
    cursor = db_conn.cursor()
    query = """
        SELECT DATE(signed_date) as date, SUM(records) as count
        FROM signed_date_records
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
        print(
            f"🚨 Найдено расхождение: Дата: {date}, ClickHouse: {ch_count}, MySQL: {mysql_count}, Разница: {diff}")
        # Здесь можно вызвать свой парсер или скачивание для исправления даты
        # Например: download_and_fix(date)
        sys.exit(0)  # Завершаем выполнение скрипта
    else:
        print("✅ Расхождений не обнаружено.")


if __name__ == "__main__":
    main()
