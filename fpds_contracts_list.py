import os
import json
import mysql.connector
from pathlib import Path
from datetime import datetime
from fpds.config import DB_CONFIG

# 🔹 Константы
SOURCE_DIR = "/Volumes/T7/data"  # Где искать JSON-файлы
DEST_DIR = "/Volumes/T7/fpds"  # Куда сохранять разбитые JSON-контракты
BATCH_SIZE = 1000  # Количество записей в батче

# ✅ Подключение к MySQL


def get_db_connection():
    """Создаёт и возвращает подключение к MySQL."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(f"⚠️ Ошибка подключения к MySQL: {e}")
        return None


# ✅ Обновление статуса файла в `fpds_file_processing_log`
def update_log_status(file_id, status, total_files_created=0):
    """Обновляет статус файла в БД."""
    conn = get_db_connection()
    if not conn:
        return

    cursor = conn.cursor()
    query = """
    UPDATE fpds_file_processing_log
    SET status = %s, total_files_created = %s, end_time = NOW()
    WHERE id = %s;
    """
    cursor.execute(query, (status, total_files_created, file_id))
    conn.commit()
    cursor.close()
    conn.close()


# ✅ Групповая вставка контрактов в `fpds_contracts_list`
def batch_insert_contracts(contract_data_list):
    """Групповая вставка контрактов в БД."""
    if not contract_data_list:
        return

    conn = get_db_connection()
    if not conn:
        return

    cursor = conn.cursor()

    query = """
    INSERT INTO fpds_contracts_list (
        partition_date, piid, modification_number, modification_date, 
        signed_date, file_path, file_size, created_at, updated_at
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), NOW());
    """

    try:
        cursor.executemany(query, contract_data_list)
        conn.commit()
    except mysql.connector.Error as e:
        print(f"❌ Ошибка вставки данных в MySQL: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# ✅ Обработка JSON-файла (парсинг и разбиение)
def process_json_file(file_path, year):
    """Обрабатывает JSON-файл: парсит, создаёт файлы контрактов и записывает логи."""
    file_name = file_path.name
    print(f"📂 Обрабатываем файл: {file_name}")

    # Читаем JSON
    try:
        with open(file_path, "r") as f:
            contracts = json.load(f)
    except Exception as e:
        print(f"❌ Ошибка чтения {file_name}: {e}")
        return None

    if not contracts:
        print(f"⚠️ Файл {file_name} пуст!")
        return None

    total_contracts = len(contracts)
    print(f"📊 Найдено {total_contracts} контрактов в файле.")

    # ✅ Записываем лог в `fpds_file_processing_log`
    conn = get_db_connection()
    if not conn:
        return None

    cursor = conn.cursor()
    query = """
    INSERT INTO fpds_file_processing_log (
        year, file_name, total_contracts_in_file, status, start_time
    ) VALUES (%s, %s, %s, 'processing', NOW());
    """
    cursor.execute(query, (year, file_name, total_contracts))
    file_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()

    # ✅ Парсим контракты и создаём файлы
    contracts_created = 0
    batch_data = []
    dest_folder = Path(DEST_DIR) / str(year)
    dest_folder.mkdir(parents=True, exist_ok=True)

    for contract in contracts:
        # 🔍 Извлекаем ключевые поля
        signed_date = contract.get("content__award__relevantContractDates__signedDate") or \
            contract.get("content__IDV__relevantContractDates__signedDate") or \
            contract.get("content__OtherTransactionAward__contractDetail__relevantContractDates__signedDate") or \
            contract.get(
                "content__OtherTransactionIDV__contractDetail__relevantContractDates__signedDate")

        piid = contract.get("content__award__awardID__awardContractID__PIID") or \
            contract.get("content__IDV__contractID__IDVID__PIID") or \
            contract.get("content__OtherTransactionAward__OtherTransactionAwardID__OtherTransactionAwardContractID__PIID") or \
            contract.get(
                "content__OtherTransactionIDV__OtherTransactionIDVID__OtherTransactionIDVContractID__PIID")

        modification_number = contract.get("content__award__awardID__awardContractID__modNumber") or \
            contract.get("content__IDV__contractID__IDVID__modNumber") or \
            contract.get("content__OtherTransactionAward__OtherTransactionAwardID__OtherTransactionAwardContractID__modNumber") or \
            contract.get(
                "content__OtherTransactionIDV__OtherTransactionIDVID__OtherTransactionIDVContractID__modNumber")

        modification_date = contract.get("modified")

        if not piid:
            print("⚠️ Контракт без PIID! Пропускаем.")
            continue

        contract_filename = f"{piid}_{modification_number or '0'}.json"
        contract_filepath = dest_folder / contract_filename

        # ✅ Записываем контракт в отдельный файл
        with open(contract_filepath, "w") as cf:
            json.dump(contract, cf, indent=2)

        # ✅ Подготавливаем данные для вставки в MySQL
        partition_date = int(
            signed_date[:4] + signed_date[5:7]) if signed_date else None
        file_size = contract_filepath.stat().st_size

        batch_data.append((
            partition_date, piid, modification_number, modification_date,
            signed_date, str(contract_filepath), file_size
        ))

        contracts_created += 1

        # 🔄 Если батч заполнен — вставляем
        if len(batch_data) >= BATCH_SIZE:
            batch_insert_contracts(batch_data)
            batch_data = []

    # 🔄 Вставляем оставшиеся данные
    if batch_data:
        batch_insert_contracts(batch_data)

    # ✅ Обновляем лог в `fpds_file_processing_log`
    if contracts_created == total_contracts:
        update_log_status(file_id, "completed", contracts_created)
    else:
        update_log_status(file_id, "failed", contracts_created)

    print(
        f"✅ Файл {file_name} обработан. Создано {contracts_created} контрактов.")
    return contracts_created


# ✅ Основной процесс обработки всех файлов
def process_all_files():
    """Обходит все папки с годами, обрабатывает JSON-файлы и записывает логи."""
    for year_folder in sorted(Path(SOURCE_DIR).iterdir()):
        if year_folder.is_dir() and year_folder.name.isdigit():
            year = int(year_folder.name)
            print(f"\n📅 Обрабатываем год {year}")

            for json_file in sorted(year_folder.glob("*.json")):
                process_json_file(json_file, year)


if __name__ == "__main__":
    process_all_files()
