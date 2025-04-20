from clickhouse_driver import Client
import time

client = Client(
    host="localhost",
    port=9000,
    user="default",
    password="",
    database="fpds_analytics"
)

start_time = time.perf_counter()

# Очистка таблицы
client.execute("TRUNCATE TABLE state_obligated_summary")

# Вставка агрегированных данных
client.execute("""
INSERT INTO state_obligated_summary (state, total_amount)
SELECT 
    concat('US-', content__award__placeOfPerformance__principalPlaceOfPerformance__stateCode) AS state,
    SUM(content__award__dollarValues__obligatedAmount) AS total_amount
FROM fpds_clickhouse.raw_contracts
WHERE content__award__placeOfPerformance__principalPlaceOfPerformance__countryCode = 'USA'
GROUP BY state

""")

end_time = time.perf_counter()
elapsed = end_time - start_time

print(f"✅ state_obligated_summary updated in {elapsed:.2f} seconds.")
