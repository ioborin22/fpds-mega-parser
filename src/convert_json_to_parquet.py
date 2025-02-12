import pandas as pd
import json
import os

# Указываем путь к JSON-файлу
json_file = "/Users/iliaoborin/fpds/data/2023-01-03/69a23cd4-a26f-4b17-ab07-5158bc8f5c18.json"

# Определяем путь для сохранения Parquet-файла (замена .json → .parquet)
parquet_file = json_file.replace(".json", ".parquet")

# Загружаем JSON
with open(json_file, "r") as f:
    data = json.load(f)

# Конвертируем в DataFrame
df = pd.DataFrame(data)

# Сохраняем в Parquet
df.to_parquet(parquet_file, engine="pyarrow", compression="snappy")  # Или "gzip", "zstd"

print(f"✅ JSON успешно конвертирован в Parquet: {parquet_file}")