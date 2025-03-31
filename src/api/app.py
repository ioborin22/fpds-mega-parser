from fastapi import FastAPI
import clickhouse_connect

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

import mysql.connector
from fpds.config import DB_CONFIG

def get_db_connection():
    """ Подключение к MySQL """
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        print(f"⚠️ Database connection error: {e}")
        return None

templates = Jinja2Templates(directory="/Users/iliaoborin/fpds/src/web/templates")

app = FastAPI()
client = clickhouse_connect.get_client(host="localhost", port=8123)


@app.get("/contract/{contract_id}")
async def get_contract(contract_id: str):
    query = f"SELECT * FROM fpds_clickhouse.raw_contracts WHERE id = toUUID('{contract_id}') LIMIT 1"
    result = client.query(query)

    if not result.result_rows:
        return {"error": "Not found"}

    # Формируем словарь и убираем `None` значения
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

@app.get("/fpds", response_class=HTMLResponse)
async def fpds_dashboard(request: Request):
    query = """
    SELECT 
        partition_year, 
        partition_month, 
        partition_day, 
        COUNT(*) as count
    FROM fpds_clickhouse.raw_contracts
    GROUP BY partition_year, partition_month, partition_day
    ORDER BY partition_year, partition_month, partition_day
    """
    result = client.query(query)

    # Группируем по годам → год -> [ { date, count }, ... ]
    grouped = {}
    for row in result.result_rows:
        year, month, day, count = row
        date_str = f"{year:04d}-{month:02d}-{day:02d}"
        if year not in grouped:
            grouped[year] = []
        grouped[year].append({
            "date": date_str,
            "count": count
        })

    return templates.TemplateResponse("main.html", {
        "request": request,
        "grouped_data": grouped
    })


# Запуск сервера:
# uvicorn src.api.app:app --reload
# http://127.0.0.1:8000/contract/474855fc-004e-4a25-8d08-bae1cfd27106
# http://127.0.0.1:8000/mutations
