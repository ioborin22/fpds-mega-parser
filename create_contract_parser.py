import re

# Путь к файлу с таблицей ClickHouse
schema_file = "/Users/iliaoborin/fpds/create_clickhouse_table.py"
output_file = "/Users/iliaoborin/fpds/src/fpds/cli/parts/contract_parser.py"

# Переменные, которые должны быть записаны с тире вместо подчеркивания
special_fields = {
    "content__award__contractData__GFE_GFP": "content__award__contractData__GFE-GFP",
    "content__award__contractData__GFE_GFP__description": "content__award__contractData__GFE-GFP__description",
    "content__IDV__contractData__GFE_GFP": "content__IDV__contractData__GFE-GFP",
    "content__IDV__contractData__GFE_GFP__description": "content__IDV__contractData__GFE-GFP__description"
}

# Переменные, которые **обязательно** должны быть в начале списка
extra_fields = [
    "partition_year", "title", "contract_type", "link__rel", "link__type", "link__href", "modified"
]

# Регулярное выражение для поиска переменных
column_pattern = re.compile(r'^\s*([\w__]+)\s+Nullable\(', re.MULTILINE)

# Читаем файл и извлекаем переменные **в порядке появления**
columns = []

with open(schema_file, "r", encoding="utf-8") as file:
    for line in file:
        match = column_pattern.search(line)
        if match:
            column_name = match.group(1)
            if column_name.startswith("content__") or column_name in extra_fields:
                if column_name not in columns:  # Исключаем дубликаты
                    columns.append(column_name)

# Убеждаемся, что **все extra_fields точно добавлены в начале**
columns = extra_fields + [col for col in columns if col not in extra_fields]

# Генерируем содержимое файла contract_parser.py
parser_text = """def extract_contract_data(contract, partition_year):
    return [
        partition_year,
"""

for col in columns[1:]:  # Первый элемент — partition_year, он уже добавлен вручную
    col_name = special_fields.get(col, col)  # Подменяем, если в special_fields
    parser_text += f'        contract.get("{col_name}"),\n'

parser_text += "    ]\n"

# Записываем в файл
with open(output_file, "w", encoding="utf-8") as file:
    file.write(parser_text)

# Выводим результат с правильным количеством переменных
print(f"✅ Файл {output_file} успешно создан.")
print(f"📊 Всего переменных: {len(columns)}")
