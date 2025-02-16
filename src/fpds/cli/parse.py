import asyncio
import json
import mysql.connector
import click
import os
import pandas as pd

from datetime import datetime
from itertools import chain
from pathlib import Path
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
    
    # Colored statuses
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
        click.echo(f"📝 Parsing status updated for {parsed_date}: {colored_status}")
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
    """Parses JSON file and saves ALL contracts to the database and as Parquet files"""

    conn = get_db_connection()
    if conn is None:
        click.echo("⚠️ Failed to connect to the database.")
        return

    cursor = conn.cursor()

    try:
        # Loading JSON
        with open(file_path, "r") as file:
            contracts = json.load(file)

        # Create a directory for contracts
        contracts_dir = Path(os.getenv("DATA_DIR", "/Users/iliaoborin/fpds/data/"))
        contracts_dir.mkdir(parents=True, exist_ok=True)

        saved_count = 0 # Successful save counter

        for contract in contracts:
            # Extract the contract identifier (PIID) or IDV_PIID
            piid = contract.get("content__award__awardID__awardContractID__PIID") or \
                   contract.get("content__IDV__contractID__IDVID__PIID")

            if not piid:
                click.echo("🚫 Contract without PIID and IDV_PIID skipped!")
                continue  # Skip contracts without identifier
            
            # Get the modification number
            mod_number = contract.get("content__award__awardID__awardContractID__modNumber")
            
            # If mod_number is not "0", not empty and not None → add to file name
            if mod_number and mod_number != "0":
                file_piid = f"{piid}_mod_{mod_number}"
            else:
                file_piid = piid # Leave the original PIID for the first version

            # Generate path to contract file
            contract_file_path = None

            # Define the path to the log file
            error_log_path = contracts_dir / "errors.log"

            try:
                contract_file_path = None
                saved_count += 1
            except Exception as file_error:
                # Generate an error message
                error_message = f"{datetime.now().isoformat()} - Contract recording error {file_piid}: {file_error}\n"
                
                # Write the error to the log file
                with open(error_log_path, "a") as error_log:
                    error_log.write(error_message)

                continue  # Move to the next contract

            # Determine the type of contract
            if "content__IDV" in contract:
                contract_type = "IDV"
            elif "content__award" in contract:
                contract_type = "AWARD"
            else:
                contract_type = "UNKNOWN"

            # Fill in the fields depending on the type of contract
            if contract_type == "IDV":
                piid = contract.get("content__award__awardID__awardContractID__PIID", None)
                idv_piid = contract.get("content__IDV__contractID__IDVID__PIID", None)
                referenced_piid = contract.get("content__award__awardID__referencedIDVID__PIID", None)
                mod_number = contract.get("content__IDV__contractID__IDVID__modNumber", None)
                transaction_number = None  # IDV contracts do not have transactionNumber
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
                idv_piid = contract.get("content__IDV__contractID__IDVID__PIID", None)
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
                error_message = f"{datetime.now().isoformat()} - ⚠️ Unknown contract type: {json.dumps(contract, indent=2, ensure_ascii=False)}\n"

                # Write the error to the log file
                with open(error_log_path, "a", encoding="utf-8") as error_log:
                    error_log.write(error_message)
                return

            # Preparing data for insertion into the DB
            contract_data = (
                piid, idv_piid, referenced_piid, mod_number, transaction_number, signed_date, 
                effective_date, current_completion_date, obligated_amount, 
                base_and_exercised_options_value, base_and_all_options_value, vendor_uei, 
                naics_code, psc_code, contracting_office_agency_id, contracting_office_id, 
                funding_requesting_agency_id, funding_requesting_office_id, 
                number_of_offers_received, extent_competed, str(Path(file_path).with_suffix(".parquet"))
            )

            # Insert into DB (no duplicates)
            try:
                cursor.executemany("""
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
                """ , [contract_data])

            except mysql.connector.IntegrityError:
                click.echo(f"⚠️ Duplicate PIID in DB {piid} found! Forcedly adding a new record.")
                cursor.executemany("""
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
                """ , [contract_data])

        conn.commit()
        click.echo(f"📄 Successfully saved {saved_count} contracts out of {len(contracts)}")

        # Remove original JSON file
        os.remove(file_path)
        click.echo(f"🗑 Deleted JSON file: {file_path}")

    except Exception as e:
        click.echo(f"⚠️ Contract parsing error: {e}")

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
    DATA_FILE = Path(os.getenv("DATA_DIR", "/Users/iliaoborin/fpds/data/")) / str(year) / f"{month}_{day}.json"
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
        DATA_DIR = Path(os.getenv("DATA_DIR", "/Users/iliaoborin/fpds/data/")) / str(year)
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        
        # Save data to file
        with open(DATA_FILE, "w") as outfile:
            json.dump(records, outfile)

        click.echo(f"📄 Saved {len(records)} records as JSON: {DATA_FILE}")

        # Convert JSON to Parquet
        parquet_file = DATA_FILE.with_suffix(".parquet")  # Replace the extension .json → .parquet

        # Load JSON
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Save to Parquet
        df.to_parquet(parquet_file, engine="pyarrow", compression="snappy")  # or "gzip", "zstd"

        click.echo(f"🎯 JSON successfully converted to Parquet: {parquet_file}")

        log_parsing_result(date, str(DATA_FILE), "completed", update=True)

        # Process and save contracts
        save_contracts_to_db(date, str(DATA_FILE))

        click.echo(f"{len(records)} records have been saved as JSON at: {DATA_FILE}")
    except Exception as e:
        log_parsing_result(date, str(DATA_FILE), "failed", update=True)
        click.echo(f"Error occurred while parsing: {e}")