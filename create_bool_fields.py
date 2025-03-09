import re

# Пути к файлам
schema_file = "/Users/iliaoborin/fpds/create_clickhouse_table.py"
output_file = "/Users/iliaoborin/fpds/src/fpds/cli/parts/bool_fields.py"

# Читаем содержимое файла со схемой таблицы
with open(schema_file, "r", encoding="utf-8") as file:
    schema_text = file.read()

# Регулярное выражение для поиска булевых полей (ищет перед Nullable(UInt8))
bool_pattern = re.compile(r'`?([\w\d_]+)`?\s+Nullable\(UInt8\)')

# Извлекаем все булевые поля
bool_fields = bool_pattern.findall(schema_text)

# Генерируем текст для записи в файл
bool_fields_text = 'bool_fields = [\n'
bool_fields_text += "\n".join([f'    "{field}",' for field in bool_fields])
bool_fields_text += "\n]"

# Записываем в файл
with open(output_file, "w", encoding="utf-8") as file:
    file.write(bool_fields_text)

print(f"Файл {output_file} успешно создан.")
