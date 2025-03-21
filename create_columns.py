import re
from pathlib import Path

# Пути к файлам
schema_file = Path("/Users/iliaoborin/fpds/create_clickhouse_table.py")
output_file = Path("/Users/iliaoborin/fpds/src/fpds/cli/parts/columns.py")

# Переменные, которые **обязательно** должны быть добавлены
extra_fields = {
    "partition_year", "partition_month", "partition_day",
    "title", "contract_type", "link__rel", "link__type", "link__href", "modified", "content__type"
}

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

# Убеждаемся, что **все `extra_fields` точно добавлены**
for field in extra_fields:
    if field not in columns:
        columns.insert(0, field)  # Вставляем их **в начало списка**

# Генерируем содержимое файла columns.py
columns_text = "columns = [\n"
columns_text += "\n".join([f'    "{col}",' for col in columns])
columns_text += "\n]"

# Записываем в файл
with output_file.open("w", encoding="utf-8") as file:
    file.write(columns_text)

# Вывод результатов в **единый стиль**
print(f"✅ Файл {output_file} успешно создан.")
print(f"📊 Всего переменных: {len(columns)}")
