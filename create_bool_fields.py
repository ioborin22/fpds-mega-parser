import re
from pathlib import Path
import sys

# ✅ Для поддержки Unicode в консоли Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# Пути к файлам (Windows)
schema_file = Path(r"C:\Users\win11\Projects\fpds\create_clickhouse_table.py")
output_file = Path(r"C:\Users\win11\Projects\fpds\src\fpds\cli\parts\bool_fields.py")

# Читаем схему таблицы
with schema_file.open("r", encoding="utf-8") as file:
    schema_text = file.read()

# Регулярка для поиска булевых полей
bool_pattern = re.compile(r'^\s*([\w__]+)\s+Nullable\(UInt8\)', re.MULTILINE)
bool_fields = bool_pattern.findall(schema_text)

# Генерируем Python-массив
bool_fields_text = 'bool_fields = [\n'
bool_fields_text += "\n".join([f'    "{field}",' for field in bool_fields])
bool_fields_text += "\n]"

# Сохраняем результат
with output_file.open("w", encoding="utf-8") as file:
    file.write(bool_fields_text)

# Вывод результата
print(f"[OK] Файл успешно создан: {output_file}")
print(f"[INFO] Всего булевых полей: {len(bool_fields)}")
