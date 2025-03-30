import time
import subprocess
import psutil


def is_script_running(script_name):
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            cmdline = proc.info.get("cmdline")
            if cmdline and script_name in " ".join(cmdline):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False


while True:
    if not is_script_running("insert_json_clickhouse.py"):
        print("▶️ Запускаем insert_json_clickhouse.py")
        subprocess.Popen(
            ["python3", "/Users/iliaoborin/fpds/insert_json_clickhouse.py"])
    else:
        # print("⏳ Скрипт уже запущен. Ждём следующую минуту...")
        time.sleep(300)
