from datetime import datetime, timedelta
import mysql.connector
from clickhouse_driver import Client

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "fpds",
}

clickhouse_client = Client(
    host="localhost",
    port=9000,
    database="fpds_clickhouse",
    user="default",
    password=""
)

def get_mysql_connection():
    return mysql.connector.connect(**DB_CONFIG)

def get_clickhouse_count(date):
    query = f"SELECT COUNT(*) FROM fpds_clickhouse.raw_contracts WHERE partition_date = toDate32('{date}')"
    result = clickhouse_client.execute(query)
    return result[0][0]

def insert_or_update(date, count):
    if count <= 0:
        print(f"⛔ Пропущено {date} — 0 записей в ClickHouse.")
        return

    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT clickhouse_records FROM signed_date_records WHERE signed_date = %s", (date,))
    row = cursor.fetchone()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if row:
        if row[0] != count:
            cursor.execute("""
                UPDATE signed_date_records 
                SET clickhouse_records = %s, updated_at = %s 
                WHERE signed_date = %s
            """, (count, now, date))
            print(f"🔄 Обновлено {date}: {count}")
        else:
            print(f"✅ {date} — без изменений")
    else:
        cursor.execute("""
            INSERT INTO signed_date_records (signed_date, clickhouse_records, updated_at) 
            VALUES (%s, %s, %s)
        """, (date, count, now))
        print(f"➕ Добавлено {date}: {count} записей")

    conn.commit()
    cursor.close()
    conn.close()


def main():
    current = datetime(1957, 10, 1).date()
    today = datetime.now().date()
    while current <= today:
        iso_date = current.isoformat()
        print(f"📅 Processing {iso_date}")
        count = get_clickhouse_count(iso_date)
        insert_or_update(iso_date, count)
        current += timedelta(days=1)

if __name__ == "__main__":
    main()
