from db import get_clickhouse_connection

client = get_clickhouse_connection()

# Проверка подключения
try:
    result = client.query("SELECT version()")
    print(f"✅ Подключение успешно! Версия ClickHouse: {result.result_rows[0][0]}")
except Exception as e:
    print(f"❌ Ошибка подключения к ClickHouse: {e}")