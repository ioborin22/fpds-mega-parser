import clickhouse_connect
import mysql.connector
from fpds.config import DB_CONFIG
import sys


def get_clickhouse_data():
    """
    Запрашивает данные из ClickHouse, группируя по дате.
    Форматирует дату как 'YYYY-MM-DD'.
    """
    client = clickhouse_connect.get_client(host="localhost", port=8123)
    query = """
        SELECT 
            partition_year, 
            partition_month, 
            partition_day, 
            COUNT(*) as count
        FROM fpds_clickhouse.raw_contracts
        GROUP BY partition_year, partition_month, partition_day
        ORDER BY partition_year, partition_month, partition_day
    """
    result = client.query(query)
    data = {}
    # Форматирование даты: используем правильный порядок: год-месяц-день
    for row in result.result_rows:
        year, month, day, count = row
        date_str = f"{year:04d}-{month:02d}-{day:02d}"
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
        # Берем первую найденную запись
        date, ch_count, mysql_count = issues[0]
        diff = ch_count - mysql_count
        print(
            f"Найдена расхождения: Дата: {date}, ClickHouse: {ch_count}, MySQL: {mysql_count}, Разница: {diff}")
        # Здесь можно добавить вызов вашего парсера для обработки данной даты
        # Например: download_and_fix(date)
        sys.exit(0)  # Завершаем выполнение скрипта
    else:
        print("Расхождений не обнаружено.")


if __name__ == "__main__":
    main()
