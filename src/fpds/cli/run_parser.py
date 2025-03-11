import time
import subprocess
import re  # Для работы с регулярными выражениями


def is_parser_running():
    """Проверяет, работает ли процесс `fpds parse clickhouse all`"""
    try:
        # Используем `pgrep -f`, чтобы найти процесс по полному названию команды
        result = subprocess.run(
            ["pgrep", "-f", "fpds parse clickhouse all"], capture_output=True, text=True)
        return result.returncode == 0  # Если процесс найден, returncode будет 0
    except Exception as e:
        print(f"Ошибка проверки запущенного парсера: {e}")
        return False


def run_parser():
    """Запускает парсер `fpds parse clickhouse all`, если он ещё не работает"""
    total_inserted = 0  # Счетчик для общего количества записей

    while True:
        if not is_parser_running():
            print("🚀 Запускаем `fpds parse clickhouse all`...")
            process = subprocess.Popen(["fpds", "parse", "clickhouse", "all"],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Чтение вывода процесса для отслеживания количества вставленных записей
            for line in process.stdout:
                # Покажем весь вывод для диагностики
                print(f"Текущий вывод: {line.strip()}")

                # Ищем строку, в которой пишется количество загруженных записей
                match = re.search(r"Загружено (\d+) контрактов", line)
                if match:
                    # Извлекаем количество вставленных записей
                    added_count = int(match.group(1))
                    total_inserted += added_count  # Обновляем общий счетчик
                    print(
                        f"✅ Загружено {added_count} записей. Всего добавлено: {total_inserted}", end="\r")

            # Если нужно отслеживать ошибки:
            for line in process.stderr:
                print(f"Ошибка: {line.strip()}")

        else:
            print("✅ Парсер уже работает. Пропускаем запуск.")

        time.sleep(1)  # Проверяем снова через 3 секунды


if __name__ == "__main__":
    run_parser()
