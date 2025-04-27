import re
from pathlib import Path
import sys

# Поддержка юникода в stdout (в безопасном режиме)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# Пути к файлам (Windows)
schema_file = Path(r"C:\Users\iobor\Projects\fpds\create_clickhouse_table.py")
output_file = Path(r"C:\Users\iobor\Projects\fpds\src\fpds\cli\parts\columns.py")

# Обязательные поля — первыми
extra_fields = [
    "partition_date",
    "title", "contract_type", "link__rel", "link__type", "link__href",
    "modified", "content__type"
]

# Регулярка: ищет поля Nullable(...)
column_pattern = re.compile(r'^\s*([\w__]+)\s+Nullable\(', re.MULTILINE)

columns = []

# Извлечение переменных из схемы
with schema_file.open("r", encoding="utf-8") as file:
    for line in file:
        match = column_pattern.search(line)
        if match:
            column_name = match.group(1)
            if column_name.startswith("content__") or column_name in extra_fields:
                if column_name not in columns:
                    columns.append(column_name)

# Упорядочим: сначала extra_fields
ordered_fields = []
for field in extra_fields:
    if field in columns:
        ordered_fields.append(field)
        columns.remove(field)
    else:
        ordered_fields.append(field)

ordered_fields.extend(columns)

# Генерация Python-файла
columns_text = "columns = [\n"
columns_text += "\n".join([f'    "{col}",' for col in ordered_fields])
columns_text += "\n]"

with output_file.open("w", encoding="utf-8") as file:
    file.write(columns_text)

# Вывод результата
print(f"[OK] Файл успешно создан: {output_file}")
print(f"[INFO] Всего переменных: {len(ordered_fields)}")
