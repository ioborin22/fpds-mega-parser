import sys
from pathlib import Path

# ✅ Добавляем путь к "src" ПЕРЕД всеми импортами
src_path = Path(__file__).resolve().parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

import ijson
import clickhouse_connect

from fpds.cli.parts.utils import process_booleans, log_missing_keys
from fpds.cli.parts.contract_parser import extract_contract_data
from fpds.cli.parts.columns import columns
from fpds.cli.parts.bool_fields import bool_fields
from datetime import datetime
import gc
import time

def insert_direct(date_str):
    year, month, day = date_str.split("-")
    file_path = Path(f"C:/Users/iobor/Projects/fpds/data/{year}/{month}_{day}.json")

    if not file_path.exists():
        print(f"❌ Файл не найден: {file_path}")
        return

    print(f"📖 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Загружаем файл: {file_path}")
    client = clickhouse_connect.get_client(host="localhost", port=8123, database="fpds_clickhouse")

    all_data = []
    inserted = 0

    with open(file_path, "r") as f:
        parser = ijson.items(f, "item")
        for contract in parser:
            signed_date_keys = [
                "content__award__relevantContractDates__signedDate",
                "content__IDV__relevantContractDates__signedDate",
                "content__OtherTransactionAward__contractDetail__relevantContractDates__signedDate",
                "content__OtherTransactionIDV__contractDetail__relevantContractDates__signedDate",
            ]
            signed_date = next((contract.get(k) for k in signed_date_keys if k in contract and contract[k]), None)
            if not signed_date:
                continue

            dt = datetime.strptime(signed_date, "%Y-%m-%d %H:%M:%S")
            contract = process_booleans(contract, bool_fields)
            contract_data = extract_contract_data(contract, dt.date())
            log_missing_keys(contract, columns, file_path)

            all_data.append(contract_data)

    if all_data:
        client.insert("raw_contracts", all_data, column_names=columns)
        inserted = len(all_data)
        print(f"✅ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Вставлено {inserted} записей")
    # 🧹 Явная очистка памяти
    del all_data, contract_data, contract, parser
    gc.collect()
    print(f"😴 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sleep 5 sec.")
    time.sleep(5)
    print(f"🏁 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Загрузка завершена.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("⚠️ Использование: python insert_json_clickhouse_direct.py YYYY-MM-DD")
        sys.exit(1)

    insert_direct(sys.argv[1])
