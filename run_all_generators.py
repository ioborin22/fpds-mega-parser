import subprocess

# Пути к скриптам
scripts = [
    r"C:\Users\iobor\Projects\fpds\create_bool_fields.py",
    r"C:\Users\iobor\Projects\fpds\create_columns.py",
    r"C:\Users\iobor\Projects\fpds\create_contract_parser.py"
]

print("🚀 Запуск генерации всех файлов...")

for script in scripts:
    print(f"\n▶️ Запуск {script} ...")
    try:
        result = subprocess.run(["python", script], capture_output=True, text=True, encoding='utf-8')
    except UnicodeDecodeError as e:
        print(f"❌ Unicode ошибка при запуске {script}: {e}")
        break

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(f"[stderr] {result.stderr}")

    if result.returncode != 0:
        print(f"❌ Ошибка при выполнении {script}")
        break

print("\n✅ Генерация завершена.")