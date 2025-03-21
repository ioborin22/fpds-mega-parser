import json
import clickhouse_connect
import gc
import time
import mysql.connector
from pathlib import Path
from datetime import datetime
from fpds.cli.parts.utils import process_booleans, log_missing_keys
from fpds.cli.parts.contract_parser import extract_contract_data
from fpds.cli.parts.columns import columns
from fpds.cli.parts.bool_fields import bool_fields
from fpds.config import DB_CONFIG


# 📌 Настройки
BATCH_SIZE = 1000  # Количество записей в батче

# ✅ Подключение к ClickHouse
print("🔄 Проверяем подключение к ClickHouse...")
try:
    client = clickhouse_connect.get_client(
        host="localhost", port=8123, database="fpds_clickhouse"
    )
    print("✅ Подключение успешно!")
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
    exit(1)


def get_db_connection():
    """Подключение к MySQL."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(f"⚠️ Ошибка подключения к БД: {e}")
        return None


def get_next_file():
    """Получает следующий файл для загрузки из MySQL."""
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
    """Обновляет статус файла в MySQL."""
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
    """Читает JSON и вставляет в ClickHouse"""
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
        return

    if not records:
        print("⚠️ Файл пуст! Пропускаем.")
        update_status(file_id, "clickhouse_load_failed")
        return

    print(f"📊 Найдено {len(records)} контрактов. Загружаем...")

    total_inserted = inserted_records
    missing_keys = set()

    for i in range(inserted_records, len(records), BATCH_SIZE):
        batch = []
        for contract in records[i:i + BATCH_SIZE]:
            contract = {k: v for k, v in contract.items()
                        if k in columns or str(v).strip()}  # Удаляем пустые значения

            # Определяем год, месяц, день
            signed_date_keys = [
                "content__award__relevantContractDates__signedDate",
                "content__IDV__relevantContractDates__signedDate",
                "content__OtherTransactionAward__contractDetail__relevantContractDates__signedDate",
                "content__OtherTransactionIDV__contractDetail__relevantContractDates__signedDate",
            ]
            signed_date = next((contract[k] for k in signed_date_keys if k in contract and contract[k]), None)
            if not signed_date:
                raise ValueError(
                    f"❌ Ошибка! В контракте отсутствует `signed_date`. Контракт: {json.dumps(contract, indent=2)}")

            # Разбиваем строку даты "YYYY-MM-DD HH:MM:SS" и извлекаем значения
            date_parts = signed_date.split(" ")[0].split("-")  # Берём только "YYYY-MM-DD"
            partition_year = int(date_parts[0])
            partition_month = int(date_parts[1])
            partition_day = int(date_parts[2])
            # 🔄 Преобразуем булевы значения
            contract = process_booleans(contract, bool_fields)

            # 📦 Формируем данные
            contract_data = extract_contract_data(
                contract, partition_year, partition_month, partition_day)

            # 📌 Переменные, которые нужно пропустить
            excluded_keys = {
                "content__award__contractData__GFE-GFP",
                "content__award__contractData__GFE-GFP__description",
                "content__IDV__contractData__GFE-GFP",
                "content__IDV__contractData__GFE-GFP__description"
            }
            # ⚠️ Проверяем, есть ли новые переменные, которых нет в `columns`
            extra_keys = {key for key in set(contract.keys()) - set(columns) if key not in excluded_keys}
            if extra_keys:
                missing_keys.update(extra_keys)

            batch.append(contract_data)

        # 🚀 Вставка в ClickHouse
        if batch:
            # 🔹 Вставка в ClickHouse
            client.insert("raw_contracts", batch, column_names=columns)
            total_inserted += len(batch)
            print(f"✅ Вставлено {total_inserted} записей.")
            gc.collect()
            time.sleep(3)  # Предотвращаем перегрузку

        # 🔄 Обновляем статус в MySQL после каждой вставки
        update_status(file_id, "clickhouse_loaded", total_inserted)

    # 🔔 Проверяем, загружены ли все данные
    if total_inserted >= expected_records:
        update_status(file_id, "clickhouse_loaded", total_inserted)
    else:
        update_status(file_id, "clickhouse_load_failed", total_inserted)

    # 🔔 Выводим предупреждение о новых переменных
    if missing_keys:
        print("⚠️ Найдены новые переменные в JSON, которых нет в `columns`:")
        for key in missing_keys:
            print(f"  - {key}")


# 🔄 Запуск
if __name__ == "__main__":
    file_data = get_next_file()

    if file_data:
        process_data_and_insert(file_data)
    else:
        print("🎉 Нет файлов для обработки. Завершение работы.")
