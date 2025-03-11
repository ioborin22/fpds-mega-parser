import asyncio
import requests
import mysql.connector
import warnings
from datetime import datetime, timedelta
from lxml import etree
from urllib.parse import urlparse, parse_qs
from pathlib import Path
from fpds.config import DB_CONFIG

warnings.filterwarnings("ignore")

BASE_URL = "https://www.fpds.gov/ezsearch/FEEDS/ATOM?s=FPDS&FEEDNAME=PUBLIC&q=LAST_MOD_DATE:[{date},{date}]"

DATA_DIR = Path("/Users/iliaoborin/fpds/data/")
BATCH_SIZE = 1000


def get_db_connection():
    """ Подключение к MySQL """
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(f"⚠️ Database connection error: {e}")
        return None


def fetch_fpds_data(date):
    """ Загружает XML-данные по указанной дате """
    url = BASE_URL.format(date=date)
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"❌ Ошибка загрузки данных для {date}: {e}")
        return None


def parse_pages(xml_data):
    """ Извлекает количество страниц из XML """
    try:
        tree = etree.fromstring(xml_data)
        last_link = tree.xpath(
            "//atom:link[@rel='last']/@href", namespaces={"atom": "http://www.w3.org/2005/Atom"})
        if last_link:
            parsed_url = urlparse(last_link[0])
            query_params = parse_qs(parsed_url.query)
            pages = int(query_params.get("start", [0])[0])
            return pages
    except Exception as e:
        print(f"⚠️ Ошибка парсинга XML: {e}")
    return 0


def insert_into_db(date, pages):
    """ Вставляет данные в таблицу last_mod_date """
    conn = get_db_connection()
    if not conn:
        return

    cursor = conn.cursor()
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = """
    INSERT INTO last_mod_date (last_mod_date, pages, updated_at)
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE pages=%s, updated_at=%s
    """
    cursor.execute(query, (date, pages, updated_at, pages, updated_at))
    conn.commit()
    cursor.close()
    conn.close()


def main():
    """ Основная функция """
    start_date = datetime(2005, 1, 1)
    today_date = datetime.now().date()
    current_date = start_date

    while current_date.date() <= today_date:
        date_str = current_date.strftime("%Y/%m/%d")
        print(f"🔍 Обработка даты: {date_str}")

        xml_data = fetch_fpds_data(date_str)
        if xml_data:
            pages = parse_pages(xml_data)
            print(f"📄 Найдено страниц: {pages}")
            insert_into_db(date_str, pages)

        current_date += timedelta(days=1)

    print("✅ Парсер завершил работу. Достигнута текущая дата.")


if __name__ == "__main__":
    main()
