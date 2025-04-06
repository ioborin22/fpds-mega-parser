import time
import subprocess
from datetime import datetime

SCRIPT_PATH = "/Users/iliaoborin/fpds/insert_json_clickhouse.py"


def start_insert_script():
    print(
        f"▶️ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Запуск скрипта вставки...")
    process = subprocess.Popen(["python3", SCRIPT_PATH])
    process.wait()
    return process.returncode


while True:
    return_code = start_insert_script()

    if return_code == 10:
        print(f"❗ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Скрипт остановился из-за лимита памяти. Ждем 5 минут...")
        time.sleep(5 * 60)  # 5 минут паузы
    elif return_code == 0:
        print(
            f"✅ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Скрипт завершился нормально.")
        time.sleep(1)  # 1 секунда паузы
    else:
        print(f"⚠️ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Скрипт завершился с ошибкой {return_code}. Ждем 10 секунд...")
        time.sleep(10)  # Ошибка - 10 секунд пауза
