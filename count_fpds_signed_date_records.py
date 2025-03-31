import requests
import mysql.connector
import warnings
from datetime import datetime, timedelta
from lxml import etree
from urllib.parse import urlparse, parse_qs
from pathlib import Path
from fpds.config import DB_CONFIG

warnings.filterwarnings("ignore")

BASE_URL = "https://www.fpds.gov/ezsearch/FEEDS/ATOM?s=FPDS&FEEDNAME=PUBLIC&q=SIGNED_DATE:[{date},{date}]"
DATA_DIR = Path("/Users/iliaoborin/fpds/data/")
BATCH_SIZE = 1000


def get_db_connection():
    """ Подключение к MySQL """
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(f"⚠️ Database connection error: {e}")
        return None


def fetch_fpds_data(date, start=None):
    """ Загружает XML-данные по указанной дате (и старту при наличии) """
    url = BASE_URL.format(date=date)
    if start is not None:
        url += f"&start={start}"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"❌ Ошибка загрузки данных для {date}: {e}")
        return None


def count_records_for_date(date):
    """ Возвращает количество записей FPDS по дате """
    xml_data = fetch_fpds_data(date)
    if not xml_data:
        return 0

    try:
        tree = etree.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        # Считаем количество <entry> в первой странице
        entries = tree.findall(".//atom:entry", namespaces=ns)
        entry_count_first = len(entries)

        # Ищем последнюю страницу
        last_link = tree.xpath("//atom:link[@rel='last']/@href", namespaces=ns)
        if not last_link:
            return entry_count_first

        # Парсим номер последней страницы
        parsed_url = urlparse(last_link[0])
        query_params = parse_qs(parsed_url.query)
        last_start = int(query_params.get("start", [0])[0])

        if last_start == 0:
            return entry_count_first

        # Получаем данные с последней страницы
        last_page_data = fetch_fpds_data(date, start=last_start)
        if not last_page_data:
            return entry_count_first

        last_tree = etree.fromstring(last_page_data)
        last_entries = last_tree.findall(".//atom:entry", namespaces=ns)
        entry_count_last = len(last_entries)

        # Считаем всего: (полных страниц * 10) + записи на последней странице
        full_pages = last_start // 10
        total_records = (full_pages * 10) + entry_count_last
        return total_records

    except Exception as e:
        print(f"⚠️ Ошибка парсинга XML для {date}: {e}")
        return 0


def insert_into_db(date, records):
    """ Вставляет данные в таблицу signed_date_records """
    if records <= 0:
        return

    conn = get_db_connection()
    if not conn:
        return

    cursor = conn.cursor()
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = """
    INSERT INTO signed_date_records (signed_date, records, updated_at)
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE records=%s, updated_at=%s
    """
    cursor.execute(query, (date, records, updated_at, records, updated_at))
    conn.commit()
    cursor.close()
    conn.close()


def main():
    """ Основная функция """
    start_date = datetime(1957, 10, 1)
    today_date = datetime.now().date()
    current_date = start_date

    while current_date.date() <= today_date:
        date_str = current_date.strftime("%Y/%m/%d")
        iso_date = current_date.strftime("%Y-%m-%d")
        print(f"🔍 Обработка даты: {date_str}")

        record_count = count_records_for_date(date_str)
        if record_count > 0:
            print(f"📄 Найдено записей: {record_count}")
            insert_into_db(iso_date, record_count)

        current_date += timedelta(days=1)

    print("✅ Парсер завершил работу. Достигнута текущая дата.")


if __name__ == "__main__":
    main()
