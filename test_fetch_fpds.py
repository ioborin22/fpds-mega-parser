import json
import asyncio
from pathlib import Path
from fpds import fpdsRequest  # Убедись, что этот импорт работает
from itertools import chain

DATA_DIR = Path("/Users/iliaoborin/fpds/data/")


def fetch_fpds_data(date):
    formatted_date = f"LAST_MOD_DATE=[{date},{date}]"
    params = dict([formatted_date.split("=")])
    request = fpdsRequest(**params, cli_run=True)
    print("🌐 Запрашиваем FPDS данные...")

    data = asyncio.run(request.data())  # data - список списков
    return list(chain.from_iterable(data))  # Делаем плоский список


def save_data_to_file(data, file_path):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as outfile:
        json.dump(data, outfile, indent=4)  # Добавим отступы для читаемости
    print(f"📄 Сохранено {len(data)} записей в JSON: {file_path}")


# 🛠 Запуск теста
if __name__ == "__main__":
    test_date = "2005/07/25"  # Тестовая дата
    year, month, day = test_date.split("/")
    file_path = DATA_DIR / year / f"{month}_{day}.json"

    print(f"🚀 Тест: скачивание FPDS данных за {test_date}")

    data = fetch_fpds_data(test_date)  # Вызываем метод
    print(f"🔍 Получено {len(data)} записей")

    if data:
        save_data_to_file(data, file_path)  # Сохраняем файл
