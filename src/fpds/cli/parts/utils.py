
import json
from pathlib import Path
import time

MISSING_PATH = Path(r"C:\Users\iobor\Projects\fpds\data")

def convert_bool(value, field_name="UNKNOWN_FIELD"):
    """
    Преобразует строковые булевы значения в 1/0.
    - "true" → 1
    - "false" → 0
    - None или пустая строка → None (NULL в ClickHouse)
    - Если значение не "true"/"false" — выводит предупреждение
    """
    if value is None or (isinstance(value, str) and value.strip() == ""):
        return None  # ClickHouse будет хранить NULL

    if isinstance(value, str):
        value_lower = value.strip().lower()
        if value_lower == "true":
            return 1
        elif value_lower == "false":
            return 0
        else:
            print(f"🚨 ПРОБЛЕМА! Поле `{field_name}` содержит неожиданное значение: {value} ({type(value)})")
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"{field_name}: {value}\n")  # Логируем ошибочное значение
            return None  # Возвращаем NULL, чтобы избежать ошибки

    if isinstance(value, (int, float)):  # Если уже число, оставляем как есть
        return int(value)

    print(f"🚨 ПРОБЛЕМА! Поле `{field_name}` содержит неизвестный формат: {value} ({type(value)})")
    return None  # По умолчанию NULL


def process_contract_data(contract):
    """
    Обрабатывает JSON контракт:
    - Пропускает пустые значения (None, "", только переносы строк)
    - Преобразует "true"/"false" в 1/0
    - Оставляет ключи, указанные в `important_keys`, даже если они пустые
    """
    processed_contract = {}

    # Переменные, которые всегда должны быть в контракте
    important_keys = {
        "title",
        "contract_type",
        "link__rel",
        "link__type",
        "link__href",
        "modified"
    }

    for key, value in contract.items():
        # Пропускаем значения, содержащие только пробелы и переносы строк
        if isinstance(value, str) and value.strip() == "":
            continue

        # Преобразуем булевы значения
        if key.startswith("content__") and isinstance(value, str):
            # <== Убедись, что функция convert_bool есть!
            processed_contract[key] = convert_bool(value)
        else:
            processed_contract[key] = value  # Оставляем другие данные как есть

    # Добавляем важные ключи, если их нет в данных
    for key in important_keys:
        if key not in processed_contract:
            processed_contract[key] = None  # Записываем NULL в ClickHouse

    return processed_contract


def process_booleans(contract, bool_fields):
    """
    🔄 Преобразует строковые булевые значения в 1/0 для всех указанных полей.
    """
    for field in bool_fields:
        if field in contract:
            try:
                # Теперь передается имя поля!
                contract[field] = convert_bool(contract[field], field)
            except Exception as e:
                print(f"❌ Ошибка в поле `{field}`: {contract[field]} → {e}")
    return contract


def clean_keys(data):
    """
    Очищает ключи JSON от пустых значений, перевода строк и незначащих символов.
    
    :param data: JSON-объект контракта
    :return: Множество "чистых" ключей
    """
    return {k for k, v in data.items() if isinstance(v, (str, list, dict)) and str(v).strip() not in ["", "\n", "\n              "]}


def log_missing_keys(contract, columns, json_file_path):
    """
    Проверяет, какие ключи из JSON-контракта отсутствуют в БД,
    сохраняет их в фиксированную папку и сообщает об этом.
    
    :param contract: JSON-объект контракта
    :param columns: Список колонок, присутствующих в ClickHouse
    :param json_file_path: Путь к оригинальному JSON-файлу
    """
    excluded_keys = {
        "content__award__contractData__GFE-GFP",
        "content__award__contractData__GFE-GFP__description",
        "content__IDV__contractData__GFE-GFP",
        "content__IDV__contractData__GFE-GFP__description"
    }

    clean_contract_keys = clean_keys(contract)

    missing_keys = {
        key: contract[key] for key in clean_contract_keys
        if key not in columns and key not in excluded_keys
    }

    if missing_keys:
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S") + f"_{int(time.time() * 1000) % 1000}"

        # Используем глобальный MISSING_PATH
        MISSING_PATH.mkdir(parents=True, exist_ok=True)

        missing_json_path = MISSING_PATH / f"{Path(json_file_path).stem}_missing_{timestamp}.json"

        with open(missing_json_path, "w", encoding="utf-8") as missing_file:
            json.dump(missing_keys, missing_file, indent=4, ensure_ascii=False)

        print(f"🚨 {len(missing_keys)} missing keys saved.")
        print(f"💾 File: {missing_json_path}")
