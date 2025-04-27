# watcher_update_all_records.py

import subprocess
import time
import sys
from pathlib import Path

SCRIPT_PATH = Path(r"C:\Users\iobor\Projects\fpds\update_all_records.py")
VENV_PYTHON = sys.executable  # Текущий Python

def start_script():
    """Запускает скрипт через Python (в этом же окне)"""
    print(f"▶️ [Watcher] Запускаю {SCRIPT_PATH}...")
    return subprocess.Popen([VENV_PYTHON, str(SCRIPT_PATH)])

def main():
    print(f"🛡 Watcher запущен. Следим за {SCRIPT_PATH}...\n")
    process = start_script()

    while True:
        if process.poll() is not None:  # Если процесс завершился
            print(f"⚠️ [Watcher] Скрипт завершился. Перезапуск...")
            process = start_script()
        time.sleep(1)

if __name__ == "__main__":
    main()
