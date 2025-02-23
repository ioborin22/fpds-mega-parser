import time
import subprocess

def is_parser_running():
    """ Проверяет, работает ли процесс парсера """
    try:
        # Используем команду `pgrep` для поиска процесса `fpds parse all`
        result = subprocess.run(["pgrep", "-f", "fpds parse all"], capture_output=True, text=True)
        return result.returncode == 0  # Если процесс найден, returncode будет 0
    except Exception as e:
        print(f"Ошибка проверки запущенного парсера: {e}")
        return False

def run_parser():
    """ Запускает парсер, если он еще не работает """
    while True:
        if not is_parser_running():
            print("🚀 Запускаем fpds parse all...")
            subprocess.Popen(["fpds", "parse", "all"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print("✅ Парсер уже работает. Пропускаем запуск.")
        
        time.sleep(3)  # Ожидаем 3 секунды перед следующей проверкой

if __name__ == "__main__":
    run_parser()