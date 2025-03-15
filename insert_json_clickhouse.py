import json
import clickhouse_connect
import gc
import time
from pathlib import Path
from datetime import datetime
from fpds.cli.parts.utils import process_booleans, log_missing_keys
from fpds.cli.parts.contract_parser import extract_contract_data
from fpds.cli.parts.columns import columns
from fpds.cli.parts.bool_fields import bool_fields

# 📌 Настройки
BATCH_SIZE = 1000  # Количество записей в батче
DATA_PATH = Path("/Volumes/Storage01/data")  # Путь к JSON

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


def find_json_file():
    """Ищем первый доступный JSON-файл."""
    for year_dir in sorted(DATA_PATH.iterdir()):
        if year_dir.is_dir():
            for json_file in sorted(year_dir.glob("*.json")):
                print(f"✅ Найден файл: {json_file}")
                return json_file
    print("⚠️ Нет JSON-файлов для загрузки.")
    exit(0)


def process_data_and_insert(file_path):
    """Читает JSON и вставляет его в ClickHouse"""
    print(f"📖 Открываем JSON-файл: {file_path}")

    with open(file_path, "r") as f:
        records = json.load(f)

    if not records:
        print("⚠️ Файл пуст! Пропускаем.")
        return

    print(f"📊 Найдено {len(records)} контрактов. Обрабатываем...")

    total_inserted = 0
    missing_keys = set()

    for i in range(0, len(records), BATCH_SIZE):
        batch = []
        for contract in records[i:i + BATCH_SIZE]:
            contract = {k: v for k, v in contract.items()
                        if k in columns or v.strip()}
            # Определяем `partition_year`
            signed_date_keys = [
                "content__award__relevantContractDates__signedDate",
                "content__IDV__relevantContractDates__signedDate",
                "content__OtherTransactionAward__contractDetail__relevantContractDates__signedDate",
                "content__OtherTransactionIDV__contractDetail__relevantContractDates__signedDate",
            ]
            signed_date = next((contract.get(k)
                               for k in signed_date_keys if k in contract), None)
            if not signed_date:
                raise ValueError(f"❌ Ошибка! В контракте отсутствует `signed_date`. Контракт: {json.dumps(contract, indent=2)}")
            
            # Берем первые 4 символа (YYYY)
            partition_year = int(signed_date[:4])

            # 🔄 Преобразуем булевы значения
            contract = process_booleans(contract, bool_fields)

            # 📦 Формируем данные
            contract_data = extract_contract_data(contract, partition_year)

            # ⚠️ Проверяем, есть ли новые переменные, которых нет в `columns`
            extra_keys = set(contract.keys()) - set(columns)
            if extra_keys:
                missing_keys.update(extra_keys)

            batch.append(contract_data)

        # 🚀 Вставка в ClickHouse
        if batch:
            client.insert("raw_contracts", batch, column_names=columns)
            total_inserted += len(batch)
            print(f"✅ Вставлено {total_inserted} записей.")
            gc.collect()
            time.sleep(2)  # Предотвращаем перегрузку

    # 🔔 Выводим предупреждение о новых переменных
    if missing_keys:
        print("⚠️ Найдены новые переменные в JSON, которых нет в `columns`:")
        for key in missing_keys:
            print(f"  - {key}")


# 🔄 Запуск
if __name__ == "__main__":
    json_file = find_json_file()  # 🗂 Находим JSON-файл
    process_data_and_insert(json_file)  # 📥 Вставляем в ClickHouse
