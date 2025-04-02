import re
from pathlib import Path

# Пути к файлам
schema_file = Path("/Users/iliaoborin/fpds/create_clickhouse_table.py")
output_file = Path("/Users/iliaoborin/fpds/src/fpds/cli/parts/columns.py")

# Переменные, которые **обязательно** должны быть добавлены, в нужном порядке
extra_fields = [
    "partition_year", "partition_month", "partition_day",
    "title", "contract_type", "link__rel", "link__type", "link__href", "modified", "content__type"
]

# Регулярное выражение для поиска колонок
column_pattern = re.compile(r'^\s*([\w__]+)\s+Nullable\(', re.MULTILINE)

# Читаем файл и извлекаем переменные **в порядке появления**
columns = []

with schema_file.open("r", encoding="utf-8") as file:
    for line in file:
        match = column_pattern.search(line)
        if match:
            column_name = match.group(1)
            if column_name.startswith("content__") or column_name in extra_fields:
                if column_name not in columns:  # Исключаем дубликаты
                    columns.append(column_name)

# Извлекаем extra_fields в нужном порядке и убираем их из columns, если они уже там
ordered_fields = []
for field in extra_fields:
    if field in columns:
        ordered_fields.append(field)
        columns.remove(field)
    else:
        # Если поля не было в columns, добавляем его всё равно
        ordered_fields.append(field)

# Добавляем оставшиеся поля после extra_fields
ordered_fields.extend(columns)

# Генерируем содержимое файла columns.py
columns_text = "columns = [\n"
columns_text += "\n".join([f'    "{col}",' for col in ordered_fields])
columns_text += "\n]"

# Записываем в файл
with output_file.open("w", encoding="utf-8") as file:
    file.write(columns_text)

# Вывод результатов в **единый стиль**
print(f"✅ Файл {output_file} успешно создан.")
print(f"📊 Всего переменных: {len(ordered_fields)}")
