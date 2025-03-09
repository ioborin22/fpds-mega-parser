import subprocess

# Пути к скриптам
scripts = [
    "/Users/iliaoborin/fpds/create_bool_fields.py",
    "/Users/iliaoborin/fpds/create_columns.py",
    "/Users/iliaoborin/fpds/create_contract_parser.py"
]

print("🚀 Запуск генерации всех файлов...")

# Запускаем каждый скрипт по очереди
for script in scripts:
    print(f"\n▶️ Запуск {script} ...")
    result = subprocess.run(["python", script], capture_output=True, text=True)

    # Выводим результат работы скрипта
    print(result.stdout)

    # Если ошибка — выводим и прерываем выполнение
    if result.returncode != 0:
        print(f"❌ Ошибка при выполнении {script}:\n{result.stderr}")
        break

print("\n✅ Генерация завершена.")
