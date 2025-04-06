import json
import clickhouse_connect
import gc
import time
import mysql.connector
import pendulum
import sys
from pathlib import Path
from datetime import datetime
from fpds.cli.parts.utils import process_booleans, log_missing_keys
from fpds.cli.parts.contract_parser import extract_contract_data
from fpds.cli.parts.columns import columns
from fpds.cli.parts.bool_fields import bool_fields
from fpds.config import DB_CONFIG

# 📌 Настройки
BATCH_SIZE = 1000
MAX_MEMORY_ERRORS = 3  # Максимально допустимое количество ошибок памяти подряд

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


def insert_batch_with_retry(client, table, batch, columns, file_id):
    wait_time = 10
    memory_error_count = 0

    while True:
        try:
            client.insert(table, batch, column_names=columns)
            memory_error_count = 0  # Успешная вставка - сбрасываем счётчик
            break
        except Exception as e:
            if "MEMORY_LIMIT_EXCEEDED" in str(e):
                memory_error_count += 1
                print(f"⚠️ Ошибка памяти #{memory_error_count}: {e}")

                if memory_error_count >= MAX_MEMORY_ERRORS:
                    print(
                        "❌ Превышено количество ошибок памяти. Останавливаем процесс!")
                    update_status(file_id, "clickhouse_memory_failed")
                    sys.exit(10)  # <<< Завершаем процесс с кодом 10
                print(f"⌛ Ждем {wait_time} секунд перед повторной попыткой...")
                time.sleep(wait_time)
                wait_time += 10
            else:
                raise


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

    try:
        with open(file_path, "r") as f:
            records = json.load(f)
    except Exception as e:
        print(f"❌ Ошибка чтения {file_path}: {e}")
        update_status(file_id, "clickhouse_load_failed")
        sys.exit(1)

    if not records:
        print("⚠️ Файл пуст! Пропускаем.")
        update_status(file_id, "clickhouse_load_failed")
        sys.exit(1)

    print(f"📊 Найдено {len(records)} контрактов. Загружаем...")

    total_inserted = inserted_records

    for i in range(inserted_records, len(records), BATCH_SIZE):
        batch = []
        for contract in records[i:i + BATCH_SIZE]:
            contract = {k: v for k, v in contract.items(
            ) if k in columns or str(v).strip()}

            signed_date_keys = [
                "content__award__relevantContractDates__signedDate",
                "content__IDV__relevantContractDates__signedDate",
                "content__OtherTransactionAward__contractDetail__relevantContractDates__signedDate",
                "content__OtherTransactionIDV__contractDetail__relevantContractDates__signedDate",
            ]
            signed_date = next((contract.get(
                k) for k in signed_date_keys if k in contract and contract[k]), None)
            if not signed_date:
                raise ValueError(
                    f"❌ Ошибка! В контракте отсутствует `signed_date`. Контракт: {json.dumps(contract, indent=2)}")

            dt = pendulum.from_format(signed_date, "YYYY-MM-DD HH:mm:ss")
            contract = process_booleans(contract, bool_fields)
            contract_data = extract_contract_data(contract, dt.date())
            log_missing_keys(contract, columns, file_path)

            batch.append(contract_data)

        if batch:
            insert_batch_with_retry(
                client, "raw_contracts", batch, columns, file_id)
            total_inserted += len(batch)
            print(f"✅ Вставлено {total_inserted} записей.")
            gc.collect()
            time.sleep(2)

            update_status(file_id, "clickhouse_loaded", total_inserted)

    if total_inserted >= expected_records:
        update_status(file_id, "clickhouse_loaded", total_inserted)
    else:
        update_status(file_id, "clickhouse_load_failed", total_inserted)


# 🔄 Запуск
if __name__ == "__main__":
    file_data = get_next_file()

    if file_data:
        process_data_and_insert(file_data)
    else:
        print("🎉 Нет файлов для обработки. Завершение работы.")
        sys.exit(0)
