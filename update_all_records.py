from datetime import datetime, timedelta
import mysql.connector
import requests
import warnings
from lxml import etree
from urllib.parse import urlparse, parse_qs
from pathlib import Path
from clickhouse_driver import Client
import time

# ---------------------- ОБЩЕЕ ---------------------- #
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

BASE_URL = "https://www.fpds.gov/ezsearch/FEEDS/ATOM?s=FPDS&FEEDNAME=PUBLIC&q=SIGNED_DATE:[{date},{date}]"
warnings.filterwarnings("ignore")

def get_mysql_connection():
    return mysql.connector.connect(**DB_CONFIG)


# ---------------------- FPDS ---------------------- #

def fetch_fpds_data(date, start=None):
    url = BASE_URL.format(date=date)
    if start is not None:
        url += f"&start={start}"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"❌ Ошибка загрузки FPDS для {date}: {e}")
        return None


def count_fpds_records(date):
    xml_data = fetch_fpds_data(date)
    if not xml_data:
        return 0

    try:
        tree = etree.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entries = tree.findall(".//atom:entry", namespaces=ns)
        entry_count_first = len(entries)

        last_link = tree.xpath("//atom:link[@rel='last']/@href", namespaces=ns)
        if not last_link:
            return entry_count_first

        parsed_url = urlparse(last_link[0])
        query_params = parse_qs(parsed_url.query)
        last_start = int(query_params.get("start", [0])[0])
        if last_start == 0:
            return entry_count_first

        last_page_data = fetch_fpds_data(date, start=last_start)
        if not last_page_data:
            return entry_count_first

        last_tree = etree.fromstring(last_page_data)
        last_entries = last_tree.findall(".//atom:entry", namespaces=ns)
        entry_count_last = len(last_entries)

        full_pages = last_start // 10
        total_records = (full_pages * 10) + entry_count_last
        return total_records

    except Exception as e:
        print(f"⚠️ Ошибка парсинга FPDS XML для {date}: {e}")
        return 0


# ---------------------- ClickHouse ---------------------- #

def get_clickhouse_count(date):
    query = f"SELECT COUNT(*) FROM fpds_clickhouse.raw_contracts WHERE partition_date = toDate32('{date}')"
    result = clickhouse_client.execute(query)
    return result[0][0]


# ---------------------- DB INSERT/UPDATE ---------------------- #

def insert_or_update(date, fpds_count, clickhouse_count):
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT fpds_records, clickhouse_records FROM signed_date_records WHERE signed_date = %s", (date,))
    row = cursor.fetchone()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if row:
        old_fpds, old_ch = row
        if old_fpds != fpds_count or old_ch != clickhouse_count:
            cursor.execute("""
                UPDATE signed_date_records 
                SET fpds_records = %s, clickhouse_records = %s, updated_at = %s 
                WHERE signed_date = %s
            """, (fpds_count, clickhouse_count, now, date))
            print(f"🔄 Обновлено {date}: FPDS={fpds_count}, CH={clickhouse_count}")
        else:
            print(f"✅ {date} — без изменений")
    else:
        cursor.execute("""
            INSERT INTO signed_date_records (signed_date, fpds_records, clickhouse_records, updated_at)
            VALUES (%s, %s, %s, %s)
        """, (date, fpds_count, clickhouse_count, now))
        print(f"➕ Добавлено {date}: FPDS={fpds_count}, CH={clickhouse_count}")

    conn.commit()
    cursor.close()
    conn.close()


# ---------------------- MAIN ---------------------- #

def main():
    start_time = time.time()

    start_date = datetime(1957, 10, 1)
    today_date = datetime.now().date()
    current_date = start_date

    while current_date.date() <= today_date:
        iso_date = current_date.strftime("%Y-%m-%d")
        fpds_format_date = current_date.strftime("%Y/%m/%d")

        print(f"\n📅 Обработка {iso_date}:")

        fpds_count = count_fpds_records(fpds_format_date)
        ch_count = get_clickhouse_count(iso_date)

        print(f"   📄 FPDS: {fpds_count}")
        print(f"   💽 ClickHouse: {ch_count}")

        if fpds_count == 0 and ch_count == 0:
            print("⛔ Пропущено — нет данных в обоих источниках.")
        else:
            insert_or_update(iso_date, fpds_count, ch_count)

        current_date += timedelta(days=1)

    elapsed = time.time() - start_time
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    print(f"\n✅ Сбор и обновление данных завершены за {minutes} мин {seconds} сек.")




if __name__ == "__main__":
    main()
