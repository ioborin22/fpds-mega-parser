import os
import clickhouse_connect

def get_clickhouse_connection():
    """Создает и возвращает соединение с ClickHouse"""
    client = clickhouse_connect.get_client(
        host=os.getenv("CLICKHOUSE_HOST", "localhost"),
        port=int(os.getenv("CLICKHOUSE_PORT", 8123)),
        username=os.getenv("CLICKHOUSE_USER", "default"),
        password=os.getenv("CLICKHOUSE_PASSWORD", "692607"),
        database=os.getenv("CLICKHOUSE_DB", "fpds_clickhouse"),
        secure=False
    )
    return client