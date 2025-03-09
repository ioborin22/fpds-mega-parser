from pathlib import Path
import re

# Пути к файлам
columns_file = Path("/Users/iliaoborin/fpds/src/fpds/cli/parts/columns.py")
contract_parser_file = Path(
    "/Users/iliaoborin/fpds/src/fpds/cli/parts/contract_parser.py")

# Читаем список колонок из columns.py
with columns_file.open("r", encoding="utf-8") as f:
    columns = set(line.strip().strip('",')
                  for line in f if line.strip().startswith('"'))

# Читаем список переменных из contract_parser.py
contract_get_pattern = re.compile(r'contract\.get\("([^"]+)"\)')
contract_fields = set()

with contract_parser_file.open("r", encoding="utf-8") as f:
    for line in f:
        match = contract_get_pattern.search(line)
        if match:
            contract_fields.add(match.group(1))  # Берем только имя поля

# Проверяем разницу
missing_in_columns = contract_fields - columns
missing_in_contract_parser = columns - contract_fields

# Выводим разницу
if missing_in_columns:
    print(
        f"🚨 В contract_parser есть {len(missing_in_columns)} переменных, которых нет в columns:")
    print("\n".join(missing_in_columns))

if missing_in_contract_parser:
    print(
        f"🚨 В columns есть {len(missing_in_contract_parser)} переменных, которых нет в contract_parser:")
    print("\n".join(missing_in_contract_parser))

if not missing_in_columns and not missing_in_contract_parser:
    print("✅ Все переменные совпадают!")
