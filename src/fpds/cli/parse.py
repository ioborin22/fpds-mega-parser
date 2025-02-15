import asyncio
import json
import mysql.connector
import click
from datetime import datetime

from itertools import chain
from pathlib import Path

import click
from click import UsageError

from fpds import fpdsRequest
from fpds.utilities import validate_kwarg
from fpds.config import DB_CONFIG

def get_db_connection():
    """Creates and returns a database connection"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as e:
        click.echo(f"⚠️ Database connection error: {e}")
        return None

def log_parsing_result(parsed_date, file_path, status, update=False):
    """Logs the parsing result in the database"""
    conn = get_db_connection()
    if conn is None:
        click.echo("⚠️ Unable to connect to the database")
        return False
    
    cursor = conn.cursor()
    
    # Цветные статусы
    status_colors = {
        "completed": "green",
        "pending": "yellow",
        "failed": "red"
    }
    
    colored_status = click.style(status, fg=status_colors.get(status, "white"))

    if update:
        cursor.execute(
            "UPDATE parser_stage SET status = %s, updated_at = NOW() WHERE parsed_date = %s",
            (status, parsed_date)
        )
        conn.commit()
        click.echo(f"📝 Parsing status updated for {parsed_date}: {colored_status}")  # Вывод цветного текста
    else:
        cursor.execute("SELECT 1 FROM parser_stage WHERE parsed_date = %s", (parsed_date,))
        exists = cursor.fetchone()

        if exists:
            click.echo(f"⚠️ Data for {parsed_date} already exists in the database. Skipping download.")
            conn.close()
            return False
        else:
            cursor.execute(
                "INSERT INTO parser_stage (parsed_date, file_path, status, created_at, updated_at) "
                "VALUES (%s, %s, %s, NOW(), NOW())",
                (parsed_date, file_path, status)
            )
            conn.commit()
            click.echo(f"✅ Data for {parsed_date} successfully added to the database with status: {colored_status}")

    conn.close()
    return True

def save_contracts_to_db(parsed_date, file_path):
    
    """Парсит JSON-файл и сохраняет ВСЕ контракты в БД и файлы"""

    conn = get_db_connection()
    if conn is None:
        click.echo("⚠️ Не удалось подключиться к базе данных")
        return

    cursor = conn.cursor()

    try:
        # Загружаем JSON
        with open(file_path, "r") as file:
            contracts = json.load(file)

        # Создаем директорию для контрактов
        contracts_dir = Path(f"/Users/iliaoborin/fpds/data/{parsed_date}/contracts")
        contracts_dir.mkdir(parents=True, exist_ok=True)

        saved_count = 0  # Счетчик успешных сохранений
        lost_contracts = []  # Пропущенные контракты
        mod_counters = {}  # Счетчик модификаций PIID

        for contract in contracts:
            # Извлекаем идентификатор контракта (PIID) или IDV_PIID
            piid = contract.get("content__award__awardID__awardContractID__PIID") or \
                   contract.get("content__IDV__contractID__IDVID__PIID")

            if not piid:
                click.echo("🚫 Пропущен контракт без PIID и IDV_PIID!")
                continue  # Пропускаем контракты без идентификатора
            
            # Получаем номер модификации
            mod_number = contract.get("content__award__awardID__awardContractID__modNumber")
            
            # Если mod_number не "0", не пустой и не None → добавляем к названию файла
            if mod_number and mod_number != "0":
                file_piid = f"{piid}_mod_{mod_number}"
            else:
                file_piid = piid  # Оставляем оригинальный PIID для первой версии

            # Генерируем путь к файлу контракта
            contract_file_path = contracts_dir / f"{file_piid}.json"

            # Определяем путь к файлу логов
            error_log_path = contracts_dir / "errors.log"

            try:
                # Записываем контракт в файл
                with open(contract_file_path, "w") as contract_file:
                    json.dump(contract, contract_file, indent=4)  # Красивый JSON

                saved_count += 1  # Увеличиваем счетчик

            except Exception as file_error:
                # Формируем сообщение ошибки
                error_message = f"{datetime.now().isoformat()} - Ошибка записи контракта {file_piid}: {file_error}\n"
                
                # Записываем ошибку в лог-файл
                with open(error_log_path, "a") as error_log:
                    error_log.write(error_message)

                continue  # Переход к следующему контракту

            # Определяем тип контракта
            if "content__IDV" in contract:
                contract_type = "IDV"
            elif "content__award" in contract:
                contract_type = "AWARD"
            else:
                contract_type = "UNKNOWN"

            # Заполняем поля в зависимости от типа контракта
            if contract_type == "IDV":
                piid = contract.get("content__award__awardID__awardContractID__PIID", None)
                idv_piid = contract.get("content__IDV__contractID__IDVID__PIID", None)
                referenced_piid = contract.get("content__award__awardID__referencedIDVID__PIID", None)
                mod_number = contract.get("content__IDV__contractID__IDVID__modNumber", None)
                transaction_number = None  # У IDV контрактов нет transactionNumber
                signed_date = contract.get("content__IDV__relevantContractDates__signedDate", None)
                effective_date = contract.get("content__IDV__relevantContractDates__effectiveDate", None)
                current_completion_date = contract.get("content__IDV__relevantContractDates__lastDateToOrder", None)
                obligated_amount = float(contract.get("content__IDV__dollarValues__obligatedAmount", 0) or 0)
                base_and_exercised_options_value = None
                base_and_all_options_value = float(contract.get("content__IDV__dollarValues__totalEstimatedOrderValue", 0) or 0)
                vendor_uei = contract.get("content__IDV__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__UEI", None)
                naics_code = contract.get("content__IDV__productOrServiceInformation__principalNAICSCode", None)
                psc_code = contract.get("content__IDV__productOrServiceInformation__productOrServiceCode", None)
                contracting_office_agency_id = contract.get("content__IDV__purchaserInformation__contractingOfficeAgencyID", None)
                contracting_office_id = contract.get("content__IDV__purchaserInformation__contractingOfficeID", None)
                funding_requesting_agency_id = contract.get("content__IDV__purchaserInformation__fundingRequestingAgencyID", None)
                funding_requesting_office_id = contract.get("content__IDV__purchaserInformation__fundingRequestingOfficeID", None)
                number_of_offers_received = int(contract.get("content__IDV__competition__numberOfOffersReceived", 0) or 0)
                extent_competed = contract.get("content__IDV__competition__extentCompeted", None)

            elif contract_type == "AWARD":
                piid = contract.get("content__award__awardID__awardContractID__PIID", None)
                idv_piid = contract.get("content__award__awardID__referencedIDVID__PIID", None)
                referenced_piid = contract.get("content__award__awardID__referencedIDVID__PIID", None)
                mod_number = contract.get("content__award__awardID__awardContractID__modNumber", None)
                transaction_number = contract.get("content__award__awardID__awardContractID__transactionNumber", None)
                signed_date = contract.get("content__award__relevantContractDates__signedDate", None)
                effective_date = contract.get("content__award__relevantContractDates__effectiveDate", None)
                current_completion_date = contract.get("content__award__relevantContractDates__currentCompletionDate", None)
                obligated_amount = float(contract.get("content__award__dollarValues__obligatedAmount", 0) or 0)
                base_and_exercised_options_value = float(contract.get("content__award__dollarValues__baseAndExercisedOptionsValue", 0) or 0)
                base_and_all_options_value = float(contract.get("content__award__totalDollarValues__totalBaseAndAllOptionsValue", 0) or 0)
                vendor_uei = contract.get("content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__UEI", None)
                naics_code = contract.get("content__award__productOrServiceInformation__principalNAICSCode", None)
                psc_code = contract.get("content__award__productOrServiceInformation__productOrServiceCode", None)
                contracting_office_agency_id = contract.get("content__award__purchaserInformation__contractingOfficeAgencyID", None)
                contracting_office_id = contract.get("content__award__purchaserInformation__contractingOfficeID", None)
                funding_requesting_agency_id = contract.get("content__award__purchaserInformation__fundingRequestingAgencyID", None)
                funding_requesting_office_id = contract.get("content__award__purchaserInformation__fundingRequestingOfficeID", None)
                number_of_offers_received = int(contract.get("content__award__competition__numberOfOffersReceived", 0) or 0)
                extent_competed = contract.get("content__award__competition__extentCompeted", None)

            else:
                error_message = f"{datetime.now().isoformat()} - ⚠️ Неизвестный тип контракта: {json.dumps(contract, indent=2, ensure_ascii=False)}\n"

                # Записываем ошибку в лог-файл
                with open(error_log_path, "a", encoding="utf-8") as error_log:
                    error_log.write(error_message)
                return

            # Подготовка данных для вставки в БД
            contract_data = (
                piid, idv_piid, referenced_piid, mod_number, transaction_number, signed_date, 
                effective_date, current_completion_date, obligated_amount, 
                base_and_exercised_options_value, base_and_all_options_value, vendor_uei, 
                naics_code, psc_code, contracting_office_agency_id, contracting_office_id, 
                funding_requesting_agency_id, funding_requesting_office_id, 
                number_of_offers_received, extent_competed, str(contract_file_path)
            )

            # Вставка в БД (без дубликатов)
            try:
                cursor.execute("""
                    INSERT INTO contracts (
                        piid, idv_piid, referenced_piid, mod_number, transaction_number, signed_date, 
                        effective_date, current_completion_date, obligated_amount, 
                        base_and_exercised_options_value, base_and_all_options_value, vendor_uei, 
                        naics_code, psc_code, contracting_office_agency_id, contracting_office_id, 
                        funding_requesting_agency_id, funding_requesting_office_id, 
                        number_of_offers_received, extent_competed, file_path, created_at, updated_at
                    ) VALUES (
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, NOW(), NOW()
                    )
                """ , contract_data)

            except mysql.connector.IntegrityError:
                click.echo(f"⚠️ Дубликат PIID в БД {piid} найден! Принудительно добавляем новую запись.")
                cursor.execute("""
                    INSERT INTO contracts (
                        piid, idv_piid, referenced_piid, mod_number, transaction_number, signed_date, 
                        effective_date, current_completion_date, obligated_amount, 
                        base_and_exercised_options_value, base_and_all_options_value, vendor_uei, 
                        naics_code, psc_code, contracting_office_agency_id, contracting_office_id, 
                        funding_requesting_agency_id, funding_requesting_office_id, 
                        number_of_offers_received, extent_competed, file_path, created_at, updated_at
                    ) VALUES (
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, NOW(), NOW()
                    )
                """ , contract_data)

        conn.commit()
        click.echo(f"📄 Успешно сохранено {saved_count} контрактов из {len(contracts)}")

    except Exception as e:
        click.echo(f"⚠️ Ошибка парсинга контрактов: {e}")

    finally:
        conn.close()

@click.command()
@click.option("-o", "--output", required=False, help="Output directory")
@click.argument("date")
def parse(date, output):
    """
    Parsing command for the FPDS Atom feed with date input

    \b
    Usage:
        $ fpds parse YYYY/MM/DD [OPTIONS]
    """

    # Check if the data already exists in the database before downloading
    year, month, day = date.split("/")
    DATA_FILE = Path(f"/Users/iliaoborin/fpds/data/{year}/{month}_{day}.json")
    if not log_parsing_result(date, str(DATA_FILE), "pending"):
        return

    formatted_date = f"SIGNED_DATE=[{date},{date}]"
    params = [formatted_date.split("=")]

    if not params:
        raise UsageError("Please provide at least one parameter")

    for _param in params:  # _param is a tuple
        name, value = _param
        _param[1] = validate_kwarg(kwarg=name, string=value)

    params_kwargs = dict(params)
    click.echo(f"🔍 Params to be used for FPDS search: {params_kwargs}")

    request = fpdsRequest(**params_kwargs, cli_run=True)
    click.echo("🌐 Retrieving FPDS records from ATOM feed...")

    try:
        data = asyncio.run(request.data())
        records = list(chain.from_iterable(data))

        # Create directory if it does not exist
        DATA_DIR = Path(f"/Users/iliaoborin/fpds/data/{year}")
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        
        # Save data to file
        with open(DATA_FILE, "w") as outfile:
            json.dump(records, outfile)

        log_parsing_result(date, str(DATA_FILE), "completed", update=True)

        # Process and save contracts
        save_contracts_to_db(date, str(DATA_FILE))

        click.echo(f"{len(records)} records have been saved as JSON at: {DATA_FILE}")
    except Exception as e:
        log_parsing_result(date, str(DATA_FILE), "failed", update=True)
        click.echo(f"Error occurred while parsing: {e}")