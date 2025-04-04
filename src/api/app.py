from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import clickhouse_connect
import mysql.connector
from fpds.config import DB_CONFIG

# 📂 Путь к HTML-шаблонам
templates = Jinja2Templates(
    directory="/Users/iliaoborin/fpds/src/web/templates")

# 🚀 FastAPI приложение
app = FastAPI()

# 🔌 Клиент ClickHouse
client = clickhouse_connect.get_client(host="localhost", port=8123)


def get_db_connection():
    """Подключение к MySQL."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(f"⚠️ Database connection error: {e}")
        return None


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


@app.get("/mutations")
async def list_mutations():
    """Возвращает список активных мутаций в ClickHouse."""
    query = """
    SELECT mutation_id, command, is_done, is_killed
    FROM system.mutations
    WHERE table = 'raw_contracts' AND database = 'fpds_clickhouse'
    """
    result = client.query(query)
    mutations = [dict(zip(result.column_names, row))
                 for row in result.result_rows]
    return {"mutations": mutations}


@app.get("/", response_class=HTMLResponse)
async def fpds_dashboard(request: Request):
    # --- Запрос к ClickHouse ---
    ch_query = """
        SELECT 
            partition_date, 
            COUNT(*) as count
        FROM fpds_clickhouse.raw_contracts
        GROUP BY partition_date
        ORDER BY partition_date
    """
    ch_result = client.query(ch_query)

    # Формируем данные ClickHouse
    clickhouse_data = {}
    for row in ch_result.result_rows:
        partition_date, count = row
        # partition_date — это объект date
        date_str = partition_date.strftime("%Y-%m-%d")
        clickhouse_data[date_str] = count

    # --- Запрос к MySQL ---
    mysql_data = {}
    db_conn = get_db_connection()
    if db_conn:
        cursor = db_conn.cursor()
        mysql_query = """
            SELECT DATE(signed_date) as date, SUM(records) as count
            FROM signed_date_records
            GROUP BY date
        """
        cursor.execute(mysql_query)
        mysql_results = cursor.fetchall()
        for row in mysql_results:
            date_val, count = row
            date_str = date_val.strftime("%Y-%m-%d")
            mysql_data[date_str] = count
        cursor.close()
        db_conn.close()

    # --- Сравнение данных ---
    all_dates = set(clickhouse_data.keys()).union(mysql_data.keys())
    comparison = []
    for date in sorted(all_dates):
        ch_count = clickhouse_data.get(date, 0)
        mysql_count = mysql_data.get(date, 0)
        difference = ch_count - mysql_count
        comparison.append({
            "date": date,
            "clickhouse_count": ch_count,
            "mysql_count": mysql_count,
            "difference": difference
        })

    return templates.TemplateResponse("main.html", {
        "request": request,
        "comparison": comparison
    })

# Запуск:
# uvicorn src.api.app:app --reload
# http://127.0.0.1:8000/contract/<uuid>
# http://127.0.0.1:8000/mutations
