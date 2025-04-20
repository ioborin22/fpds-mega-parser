import time
from clickhouse_driver import Client

client = Client(
    host="localhost",
    port=9000,
    user="default",
    password="",
    database="fpds_analytics"
)

start = time.time()

# Очищаем таблицу
client.execute("TRUNCATE TABLE contract_type_summary")

# Вставка
client.execute("""
INSERT INTO contract_type_summary (type, value)
SELECT * FROM (
    SELECT 'AWARD' AS type, countIf(contract_type = 'AWARD') AS value
    FROM fpds_clickhouse.raw_contracts
    UNION ALL
    SELECT 'IDV', countIf(contract_type = 'IDV')
    FROM fpds_clickhouse.raw_contracts
    UNION ALL
    SELECT 'OTHERTRANSACTIONAWARD', countIf(contract_type = 'OTHERTRANSACTIONAWARD')
    FROM fpds_clickhouse.raw_contracts
    UNION ALL
    SELECT 'OTHERTRANSACTIONIDV', countIf(contract_type = 'OTHERTRANSACTIONIDV')
    FROM fpds_clickhouse.raw_contracts
    UNION ALL
    SELECT 'TOTAL', COUNT(*) FROM fpds_clickhouse.raw_contracts
)
""")

end = time.time()
print(f"✅ fpds_analytics.contract_type_summary table updated successfully in {end - start:.2f} seconds.")
