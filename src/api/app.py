from fastapi import FastAPI
import clickhouse_connect

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

# Запуск сервера:
# uvicorn src.api.app:app --reload
# http://127.0.0.1:8000/contract/474855fc-004e-4a25-8d08-bae1cfd27106
