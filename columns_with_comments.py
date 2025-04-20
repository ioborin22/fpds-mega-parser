import re
import json
import os
from collections import OrderedDict
from pathlib import Path

# Файлы
schema_file = Path(r"C:\Users\win11\Projects\fpds\create_clickhouse_table.py")
output_file = Path(r"C:\Users\win11\Projects\fpds\documentation\clickhouse\columns_all.json")
output_file.parent.mkdir(parents=True, exist_ok=True)

# Обязательные поля — в начале
extra_fields = [
    "partition_date",
    "title", "contract_type", "link__rel", "link__type", "link__href",
    "modified", "content__type"
]

# Регулярка: ищем строку с полем и COMMENT
column_pattern = re.compile(
    r"^\s*([\w\d__]+)\s+\w+(?:\([^\)]*\))?(?:\s+DEFAULT\s+[^C\n]+)?\s+COMMENT\s+'([^']+)'",
    re.UNICODE
)


# Регулярка для всех Nullable-полей
nullable_pattern = re.compile(r'^\s*([\w__]+)\s+Nullable\(', re.MULTILINE)

# Получаем комментарии
comments = {}
with schema_file.open("r", encoding="utf-8") as f:
    for line in f:
        match = column_pattern.search(line)
        if match:
            column = match.group(1)
            comment = match.group(2)
            comments[column] = comment

# Получаем список колонок (как в генераторе contract_parser)
columns = []
with schema_file.open("r", encoding="utf-8") as f:
    for line in f:
        match = nullable_pattern.search(line)
        if match:
            column = match.group(1)
            if column.startswith("content__") or column in extra_fields:
                if column not in columns:
                    columns.append(column)

# Финальный словарь
ordered_columns = OrderedDict()

for field in extra_fields:
    if field in columns:
        ordered_columns[field] = comments.get(field, "")
        columns.remove(field)
    else:
        ordered_columns[field] = ""

for field in columns:
    ordered_columns[field] = comments.get(field, "")

# Сохраняем в JSON
with output_file.open("w", encoding="utf-8") as f:
    json.dump(ordered_columns, f, indent=2, ensure_ascii=False)

print(f"[OK] Сохранено в: {output_file}")
print(f"[INFO] Всего полей: {len(ordered_columns)}")
