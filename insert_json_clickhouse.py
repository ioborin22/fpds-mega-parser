import os
import traceback
import json
import clickhouse_connect
import time
import mysql.connector
import pendulum
import sys
import ijson
from pathlib import Path
from datetime import datetime
from fpds.cli.parts.utils import process_booleans, log_missing_keys
from fpds.cli.parts.contract_parser import extract_contract_data
from fpds.cli.parts.columns import columns
from fpds.cli.parts.bool_fields import bool_fields
from fpds.config import DB_CONFIG

LOG_FILE = os.path.join(os.path.dirname(__file__), 'error_log.txt')

def log_error_to_file(error_msg, file_path):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"\n[{timestamp}] ❌ Ошибка обработки файла: {file_path}\n")
        f.write(error_msg)
        f.write('\n' + '='*80 + '\n')

# ✅ Подключение к ClickHouse
print("🔄 Проверяем подключение к ClickHouse...")
try:
    client = clickhouse_connect.get_client(
        host="localhost", port=8123, database="fpds_clickhouse"
    )
    print("✅ Подключение успешно!")
except Exception as e:
    print(f"❌ Ошибка подключения к ClickHouse: {e}")
    sys.exit(1)

def get_db_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(f"⚠️ Ошибка подключения к БД: {e}")
        return None

def get_next_file():
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT id, signed_date, record_count, inserted_records, file_path, status
    FROM insert_json_clickhouse
    WHERE status = 'file_found'
    ORDER BY signed_date ASC
    LIMIT 1;
    """
    cursor.execute(query)
    file_data = cursor.fetchone()
    cursor.close()
    conn.close()

    if file_data:
        print(
            f"📂 Найден файл для загрузки: {file_data['file_path']} ({file_data['record_count']} записей)")
    return file_data


def update_status(file_id, status, inserted_records=0):
    conn = get_db_connection()
    if not conn:
        return

    cursor = conn.cursor()
    query = """
    UPDATE insert_json_clickhouse
    SET status = %s, inserted_records = %s, updated_at = NOW()
    WHERE id = %s;
    """
    cursor.execute(query, (status, inserted_records, file_id))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"📌 Статус обновлен: {status}")


def process_data_and_insert(file_data):
    file_path = Path(file_data["file_path"])
    file_id = file_data["id"]
    expected_records = file_data["record_count"]
    inserted_records = file_data["inserted_records"]

    if inserted_records >= expected_records:
        print(f"✅ Все записи уже загружены для {file_path}, пропускаем.")
        update_status(file_id, "clickhouse_loaded", inserted_records)
        return

    print(f"📖 Открываем JSON-файл: {file_path}")

    total_inserted = 0
    all_data = []
    partition_date = None

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            for idx, contract in enumerate(data):
                if idx < inserted_records:
                    continue

                contract = {k: v for k, v in contract.items()
                            if k in columns or str(v).strip()}

                signed_date_keys = [
                    "content__award__relevantContractDates__signedDate",
                    "content__IDV__relevantContractDates__signedDate",
                    "content__OtherTransactionAward__contractDetail__relevantContractDates__signedDate",
                    "content__OtherTransactionIDV__contractDetail__relevantContractDates__signedDate",
                ]
                signed_date = next((contract.get(k)
                                    for k in signed_date_keys if k in contract and contract[k]), None)
                if not signed_date:
                    raise ValueError(
                        f"❌ Ошибка! В контракте отсутствует `signed_date`. Контракт: {json.dumps(contract, indent=2)}")

                dt = pendulum.from_format(signed_date, "YYYY-MM-DD HH:mm:ss")

                # запоминаем partition_date из первой записи
                if not partition_date:
                    partition_date = dt.to_date_string()

                contract = process_booleans(contract, bool_fields)
                contract_data = extract_contract_data(contract, dt.date())
                log_missing_keys(contract, columns, file_path)

                all_data.append(contract_data)

        if not all_data:
            print("⚠️ Нет новых данных для вставки.")
            update_status(file_id, "clickhouse_loaded", inserted_records)
            return

        # ✅ Удаление партиции до вставки
        if partition_date:
            print(f"🗑 Удаляем партицию: {partition_date}")
            client.command(f"ALTER TABLE raw_contracts DROP PARTITION '{partition_date}'")
            print("✅ Партиция удалена.")
        else:
            print("⚠️ partition_date не определена — пропуск удаления партиции.")

        # ✅ Вставка всех данных
        client.insert("raw_contracts", all_data, column_names=columns)
        total_inserted = len(all_data)
        update_status(file_id, "clickhouse_loaded", total_inserted)
        print(f"✅ Файл полностью загружен: {total_inserted} записей")

    except Exception as e:
        full_trace = traceback.format_exc()
        print(f"❌ Ошибка обработки файла: {e}")
        log_error_to_file(full_trace, str(file_path))
        update_status(file_id, "clickhouse_load_failed", total_inserted)



# 🔄 Запуск
if __name__ == "__main__":
    file_data = get_next_file()

    if file_data:
        process_data_and_insert(file_data)
    else:
        print("🎉 Нет файлов для обработки. Завершение работы.")
        sys.exit(0)
