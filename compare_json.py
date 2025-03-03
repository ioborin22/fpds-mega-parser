import json
import requests

# 📌 Пути к данным
LOCAL_JSON_PATH = "/Users/iliaoborin/fpds/data/1957/10_01.json"
CLICKHOUSE_URL = "http://127.0.0.1:8000/contract/e7c6dbf9-871f-46bd-b787-3dfb8668ada3"

# 🔍 Загружаем локальный JSON
with open(LOCAL_JSON_PATH, "r") as file:
    local_data = json.load(file)

# 📌 Если локальный JSON содержит список объектов, берем первый контракт
if isinstance(local_data, list):
    local_data = local_data[0]

# 🔗 Загружаем JSON из ClickHouse
response = requests.get(CLICKHOUSE_URL)
if response.status_code == 200:
    ch_data = response.json()
else:
    print(f"❌ Ошибка загрузки JSON из ClickHouse: {response.status_code}")
    exit()

# ✅ Функция очистки "мусорных" ключей (пустые строки и переносы)


def clean_keys(data):
    return {k for k, v in data.items() if isinstance(v, (str, list, dict)) and v.strip() not in ["", "\n", "\n              "]}


# 📌 Фильтруем ключи
filtered_local_keys = clean_keys(local_data)
ch_keys = set(ch_data.keys())

# 🔎 Сравнение полей
missing_in_ch = filtered_local_keys - ch_keys

# 🔥 Вывод недостающих переменных
if missing_in_ch:
    print("⚠️ В ClickHouse отсутствуют следующие переменные (игнорированы пустые `\\n`):")
    for key in sorted(missing_in_ch):
        print(f"   - {key}")
else:
    print("✅ Все переменные из локального JSON есть в ClickHouse!")
