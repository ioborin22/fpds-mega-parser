from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from clickhouse_driver import Client
import mysql.connector
from fpds.config import DB_CONFIG

from xml.etree import ElementTree as ET

# 📂 Путь к HTML-шаблонам
templates = Jinja2Templates(
    directory=r"C:\Users\iobor\Projects\fpds\src\web\templates"
)

# 🚀 FastAPI приложение
app = FastAPI()

# 🔌 Клиент ClickHouse (TCP порт 9000 по умолчанию)
client = Client(
    host="localhost",
    port=9000,
    database="fpds_clickhouse",
    user="default",
    password=""
)

def get_db_connection():
    """Подключение к MySQL."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(f"⚠️ Database connection error: {e}")
        return None

@app.get("/", response_class=HTMLResponse)
async def fpds_dashboard(request: Request):
    db_conn = get_db_connection()
    if not db_conn:
        return HTMLResponse(content="<h2>❌ Ошибка подключения к MySQL</h2>", status_code=500)

    comparison = []
    cursor = db_conn.cursor()
    query = """
        SELECT signed_date, fpds_records, clickhouse_records
        FROM signed_date_records
        ORDER BY signed_date DESC
    """
    cursor.execute(query)
    for signed_date, fpds, ch in cursor.fetchall():
        comparison.append({
            "date": signed_date.strftime("%Y-%m-%d"),
            "fpds_count": fpds,
            "clickhouse_count": ch,
            "difference": ch - fpds
        })
    cursor.close()
    db_conn.close()

    return templates.TemplateResponse("main.html", {
        "request": request,
        "comparison": comparison
    })


# Singl contract view
@app.get("/contract/{contract_id}")
async def get_contract(contract_id: str):
    query = f"SELECT * FROM fpds_clickhouse.raw_contracts WHERE id = toUUID('{contract_id}') LIMIT 1"
    result = client.query(query)

    if not result.result_rows:
        return {"error": "Not found"}

    # Формируем словарь и убираем None значения
    contract_data = dict(zip(result.column_names, result.result_rows[0]))
    filtered_data = {key: value for key,
                     value in contract_data.items() if value is not None}

    return filtered_data


def format_bytes(size):
    """Форматирует байты в KB, MB, GB и т.д."""
    power = 1024
    n = 0
    power_labels = ['B', 'KB', 'MB', 'GB', 'TB']
    while size >= power and n < len(power_labels) - 1:
        size /= power
        n += 1
    return f"{size:.2f} {power_labels[n]}"

# Функция для рекурсивного парсинга config.xml
def parse_clickhouse_config(path_to_config):
    config_data = {}
    try:
        tree = ET.parse(path_to_config)
        root = tree.getroot()
        for section in root:
            section_name = section.tag
            config_data[section_name] = {}
            for child in section:
                config_data[section_name][child.tag] = child.text or ''
    except Exception as e:
        print(f"⚠️ Ошибка при чтении конфига: {e}")
    return config_data

@app.get("/clickhouse", response_class=HTMLResponse)
async def clickhouse_info(request: Request):
    """Панель мониторинга ClickHouse."""

    # Чтение конфига ClickHouse
    def parse_clickhouse_config(path_to_config):
        config_data = {}
        try:
            tree = ET.parse(path_to_config)
            root = tree.getroot()
            for section in root:
                section_name = section.tag
                config_data[section_name] = {}
                for child in section:
                    config_data[section_name][child.tag] = child.text or ''
        except Exception as e:
            print(f"⚠️ Ошибка при чтении конфига: {e}")
        return config_data

    # Путь до твоего конфига
    config_path = '/Users/iliaoborin/clickhouse/25.2.1.3085-stable/preprocessed_configs/config.xml'
    clickhouse_config = parse_clickhouse_config(config_path)

    try:
        # 1. Версия ClickHouse
        version = client.query("SELECT version()").result_rows[0][0]

        # 2. Важные настройки
        settings_query = """
            SELECT name, value
            FROM system.settings
            WHERE name IN ('max_memory_usage', 'max_threads', 'max_server_memory_usage', 'max_memory_usage_for_all_queries', 'mark_cache_size', 'uncompressed_cache_size')
        """
        settings_result = client.query(settings_query)
        settings = {name: value for name, value in settings_result.result_rows}

        # 3. Активные запросы
        active_queries = client.query(
            "SELECT count() FROM system.processes").result_rows[0][0]

        # 4. Размер базы данных
        db_size_result = client.query("""
            SELECT sum(bytes_on_disk) AS total_bytes, sum(rows) AS total_rows
            FROM system.parts
            WHERE database = 'fpds_clickhouse'
        """)
        total_bytes, total_rows = db_size_result.result_rows[0]
        formatted_total_bytes = format_bytes(total_bytes)

        # 5. Аптайм сервера
        uptime_result = client.query(
            "SELECT formatReadableTimeDelta(uptime())").result_rows[0][0]

        # 6. Использование дисков
        disks_query = "SELECT name, free_space, total_space FROM system.disks"
        disks_result = client.query(disks_query)
        disks = [{
            "name": row[0],
            "free_space": format_bytes(row[1]),
            "total_space": format_bytes(row[2])
        } for row in disks_result.result_rows]

        # 7. Загрузка CPU
        cpu_query = "SELECT metric, value FROM system.metrics WHERE metric LIKE '%CPU%'"
        cpu_result = client.query(cpu_query)
        cpu_metrics = {metric: value for metric,
                       value in cpu_result.result_rows}

        # 8. Ошибки сервера
        errors_result = client.query("""
            SELECT value
            FROM system.events
            WHERE event = 'ExceptionWhileProcessing'
        """)
        server_errors = errors_result.result_rows[0][0] if errors_result.result_rows else 0

        # 9. Статистика кеша
        try:
            cache_query = """
                SELECT cache_name, hits, misses, round(hits / (hits + misses + 0.001), 3) as hit_ratio
                FROM system.cache_diagnostics
            """
            cache_result = client.query(cache_query)
            cache_stats = [{
                "cache_name": row[0],
                "hits": row[1],
                "misses": row[2],
                "hit_ratio": row[3]
            } for row in cache_result.result_rows]
        except Exception as e:
            print(f"⚠️ Не удалось получить кеш-статистику: {e}")
            cache_stats = []

        return templates.TemplateResponse("clickhouse.html", {
            "request": request,
            "version": version,
            "settings": settings,
            "active_queries": active_queries,
            "total_bytes": formatted_total_bytes,
            "total_rows": total_rows,
            "uptime": uptime_result,
            "disks": disks,
            "cpu_metrics": cpu_metrics,
            "server_errors": server_errors,
            "cache_stats": cache_stats,
            "clickhouse_config": clickhouse_config  # <<< Передаём!
        })

    except Exception as e:
        print(f"❌ ClickHouse недоступен: {e}")
        return templates.TemplateResponse("clickhouse.html", {
            "request": request,
            "clickhouse_running": False,
            "clickhouse_config": clickhouse_config
        })
    
@app.get("/contracts-descriptions", response_class=HTMLResponse)
async def contracts_descriptions(request: Request):
    import json

    json_path = r"C:\Users\iobor\Projects\fpds\documentation\clickhouse\columns_all.json"

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            columns_data = json.load(f)
    except Exception as e:
        return HTMLResponse(content=f"<h2>Ошибка загрузки JSON: {e}</h2>", status_code=500)

    # Общие поля
    common_fields = [
        "id", "partition_date", "title", "contract_type",
        "link__rel", "link__type", "link__href", "modified", "content__type"
    ]

    # Подготовка групп
    tabs = {
        "AWARD": [],
        "IDV": [],
        "OTHERTRANSACTIONAWARD": [],
        "OTHERTRANSACTIONIDV": []
    }

    for field, description in columns_data.items():
        if field in common_fields:
            continue
        if field.startswith("content__award__"):
            tabs["AWARD"].append((field, description))
        elif field.startswith("content__IDV__"):
            tabs["IDV"].append((field, description))
        elif field.startswith("content__OtherTransactionAward__"):
            tabs["OTHERTRANSACTIONAWARD"].append((field, description))
        elif field.startswith("content__OtherTransactionIDV__"):
            tabs["OTHERTRANSACTIONIDV"].append((field, description))

    # Вывод шаблона
    return templates.TemplateResponse("contracts-descriptions.html", {
        "request": request,
        "common": [(f, columns_data.get(f, "")) for f in common_fields],
        "tabs": tabs
    })

@app.get("/sql", response_class=HTMLResponse)
async def get_sql_page(request: Request):
    return templates.TemplateResponse("sql.html", {"request": request})


# Запуск:
# uvicorn src.api.app:app --reload
# http://127.0.0.1:8000/contract/<uuid>
# http://127.0.0.1:8000/mutations
