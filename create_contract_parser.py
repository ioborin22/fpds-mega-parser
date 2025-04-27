import re
import sys
from pathlib import Path

# Безопасная настройка stdout (на случай unicode в Windows)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# Пути к файлам (Windows)
schema_file = Path(r"C:\Users\iobor\Projects\fpds\create_clickhouse_table.py")
output_file = Path(r"C:\Users\iobor\Projects\fpds\src\fpds\cli\parts\contract_parser.py")

# Специальные подстановки с тире
special_fields = {
    "content__award__contractData__GFE_GFP": "content__award__contractData__GFE-GFP",
    "content__award__contractData__GFE_GFP__description": "content__award__contractData__GFE-GFP__description",
    "content__IDV__contractData__GFE_GFP": "content__IDV__contractData__GFE-GFP",
    "content__IDV__contractData__GFE_GFP__description": "content__IDV__contractData__GFE-GFP__description"
}

# Поля, которые должны быть первыми
extra_fields = [
    "partition_date",
    "title", "contract_type", "link__rel", "link__type", "link__href", "modified"
]

# Регулярка для поиска колонок Nullable(...)
column_pattern = re.compile(r'^\s*([\w__]+)\s+Nullable\(', re.MULTILINE)

# Сбор всех колонок
columns = []

with schema_file.open("r", encoding="utf-8") as file:
    for line in file:
        match = column_pattern.search(line)
        if match:
            column_name = match.group(1)
            if column_name.startswith("content__") or column_name in extra_fields:
                if column_name not in columns:
                    columns.append(column_name)

# Упорядочим: сначала extra_fields
columns = extra_fields + [col for col in columns if col not in extra_fields]

# Генерация текста функции
parser_text = """def extract_contract_data(contract, partition_date):
    return [
        partition_date,
"""

for col in columns[1:]:  # первая уже вручную
    col_name = special_fields.get(col, col)
    parser_text += f'        contract.get("{col_name}", None),\n'

parser_text += "    ]\n"

# Сохраняем
with output_file.open("w", encoding="utf-8") as file:
    file.write(parser_text)

print(f"[OK] Файл успешно создан: {output_file}")
print(f"[INFO] Всего переменных: {len(columns)}")
