import time
import subprocess
from datetime import datetime
import sys
from pathlib import Path

# Путь к основному скрипту
SCRIPT_PATH = Path(r"C:\Users\iobor\Projects\fpds\fpds_sync_checker.py")

# Путь к интерпретатору Python в активированном окружении
VENV_PYTHON = sys.executable

def start_insert_script():
    """
    Запускает основной скрипт через subprocess и ждет его завершения.
    """
    print(f"▶️ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Запуск скрипта вставки...")
    try:
        process = subprocess.Popen([VENV_PYTHON, str(SCRIPT_PATH)])
        process.wait()
        return process.returncode
    except Exception as e:
        print(f"❗ Ошибка запуска скрипта: {e}")
        return -1

def main():
    print(f"🛡 Watcher запущен. Следим за {SCRIPT_PATH}...\n")

    while True:
        return_code = start_insert_script()

        if return_code == 10:
            print(f"❗ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Скрипт остановился из-за лимита памяти. Ждем 5 минут...")
            time.sleep(5 * 60)
        elif return_code == 0:
            print(f"▶️ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Скрипт завершился нормально. Ждем 1 секунду...")
            print(f"⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️")
            time.sleep(1)
        else:
            print(f"⚠️ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Скрипт завершился с ошибкой {return_code}. Ждем 10 секунд...")
            time.sleep(10)

if __name__ == "__main__":
    main()
