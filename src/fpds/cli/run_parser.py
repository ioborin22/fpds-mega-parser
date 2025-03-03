import time
import subprocess


def is_parser_running():
    """ Проверяет, работает ли процесс `fpds parse clickhouse all` """
    try:
        # Используем `pgrep -f`, чтобы найти процесс по полному названию команды
        result = subprocess.run(
            ["pgrep", "-f", "fpds parse clickhouse all"], capture_output=True, text=True)
        return result.returncode == 0  # Если процесс найден, returncode будет 0
    except Exception as e:
        print(f"Ошибка проверки запущенного парсера: {e}")
        return False


def run_parser():
    """ Запускает парсер `fpds parse clickhouse all`, если он ещё не работает """
    while True:
        if not is_parser_running():
            print("🚀 Запускаем `fpds parse clickhouse all`...")
            subprocess.Popen(["fpds", "parse", "clickhouse", "all"],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print("✅ Парсер уже работает. Пропускаем запуск.")

        time.sleep(3)  # Проверяем снова через 3 секунды


if __name__ == "__main__":
    run_parser()
