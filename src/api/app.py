from fastapi import FastAPI
import clickhouse_connect

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="/Users/iliaoborin/fpds/src/templates")

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


@app.get("/signed/{date}")
async def get_signed_contracts_count(date: str):
    query = f"""
    SELECT COUNT(*)
    FROM fpds_clickhouse.raw_contracts
    WHERE arrayExists(x -> toDate(x) = '{date}', [
        content__award__relevantContractDates__signedDate,
        content__IDV__relevantContractDates__signedDate,
        content__OtherTransactionAward__contractDetail__relevantContractDates__signedDate,
        content__OtherTransactionIDV__contractDetail__relevantContractDates__signedDate
    ])
    """

    result = client.query(query)
    count = result.result_rows[0][0] if result.result_rows else 0

    return {"date": date, "contracts_count": count}


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


@app.delete("/mutations/{mutation_id}")
async def delete_mutation(mutation_id: str):
    """Удаляет указанную мутацию (нужно вручную удалять файлы)."""
    try:
        # Удаляем файл мутации вручную в файловой системе (если ClickHouse не поддерживает KILL MUTATION)
        import os
        mutation_file = f"/Users/iliaoborin/clickhouse/data/store/bc6/bc6b8dbf-e5e9-4cf3-b1f5-fc400f3ef9a2/{mutation_id}.txt"
        if os.path.exists(mutation_file):
            os.remove(mutation_file)
            return {"status": "success", "message": f"Mutation {mutation_id} deleted."}
        else:
            return {"status": "error", "message": "Mutation file not found."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.delete("/mutations")
async def delete_all_mutations():
    """Удаляет все мутации."""
    try:
        import os
        import glob
        mutation_files = glob.glob(
            "/Users/iliaoborin/clickhouse/data/store/**/mutation_*.txt", recursive=True)
        for file in mutation_files:
            os.remove(file)
        return {"status": "success", "message": "All mutations deleted."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

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
