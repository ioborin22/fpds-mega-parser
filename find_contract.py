import json
from pathlib import Path

# Указываем путь к исходному JSON-файлу
input_file = Path(r"D:\data\2022\06_09.json")

# Путь для сохранения найденного контракта
output_file = Path("C:/Users/iobor/Projects/fpds/data") / \
f"{input_file.stem}_filtered.json"


def find_and_save_contract(input_path, output_path, target_key):
    """
    Ищет первый JSON-контракт, содержащий заданный ключ, и сохраняет его в отдельный файл.

    :param input_path: Путь к исходному JSON-файлу
    :param output_path: Путь для сохранения найденного JSON
    :param target_key: Ключ, по которому выполняется поиск
    """
    try:
        # Читаем JSON-файл
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Проходим по контрактам
        for contract in data:
            if target_key in contract:
                # Сохраняем найденный контракт в отдельный файл
                with open(output_path, "w", encoding="utf-8") as out_f:
                    json.dump(contract, out_f, indent=4, ensure_ascii=False)

                print(f"✅ Контракт найден и сохранен в {output_path}")
                return  # Останавливаемся после первого найденного контракта

        print("⚠️ Контракт с указанным ключом не найден.")

    except FileNotFoundError:
        print(f"❌ Ошибка: файл {input_path} не найден.")
    except json.JSONDecodeError:
        print(f"❌ Ошибка: некорректный JSON в файле {input_path}.")


# Запуск скрипта
find_and_save_contract(input_file, output_file,
                       "content__IDV__vendor__vendorSiteDetails__divisionNumberOrOfficeCode")
