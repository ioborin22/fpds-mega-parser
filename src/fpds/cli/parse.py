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

            # Fill in the fields depending on the type of contract
            if contract.get("contract_type") == "AWARD":
                # Тип контракта (например, AWARD, IDV, OTHERTRANSACTIONAWARD, OTHERTRANSACTIONIDV).
                contract_type = contract.get("contract_type", None)
                # Дата и время последнего изменения данных о контракте.
                modified = contract.get("modified", None)
                # Код агентства, заключившего контракт.
                agency_id = contract.get("content__award__awardID__awardContractID__agencyID", None)
                # Уникальный идентификатор контракта (Procurement Instrument Identifier, PIID).
                piid = contract.get("content__award__awardID__awardContractID__PIID", None)
                # Номер модификации контракта.
                mod_number = contract.get("content__award__awardID__awardContractID__modNumber", None)
                # IDV
                idv_piid = contract.get("content__IDV__contractID__IDVID__PIID", None)
                # PIID для родительского контракта
                referenced_piid = contract.get("content__award__awardID__referencedIDVID__PIID", None)
                # Дата подписания контракта.
                signed_date = contract.get("content__award__relevantContractDates__signedDate", None)
                # Дата вступления контракта в силу.
                effective_date = contract.get("content__award__relevantContractDates__effectiveDate", None)
                # Окончательная дата завершения контракта, учитывая все возможные продления.
                ultimate_completion_date = contract.get("content__award__relevantContractDates__ultimateCompletionDate", None)
                # Сумма, фактически выделенная по контракту (обязательства по оплате).
                obligated_amount = float(contract.get("content__award__dollarValues__obligatedAmount", 0) or 0)
                # Полная стоимость контракта, включая все возможные опции (даже если они ещё не активированы).
                base_and_all_options_value = float(contract.get("content__award__dollarValues__baseAndAllOptionsValue", 0) or 0)
                # Общая сумма, выделенная по контракту (включает все модификации и изменения).
                total_obligated_amount = float(contract.get("content__award__totalDollarValues__totalObligatedAmount", 0) or 0)
                # Полная стоимость контракта, включая базовую сумму и все возможные опции (даже если они не активированы).
                total_base_and_all_options_value = float(contract.get("content__award__totalDollarValues__totalBaseAndAllOptionsValue", 0) or 0)
                # Код агентства, заключившего контракт.
                contracting_office_agency_id = contract.get("content__award__purchaserInformation__contractingOfficeAgencyID", None)
                # Код контрактного офиса, который оформил контракт.
                contracting_office_id = contract.get("content__award__purchaserInformation__contractingOfficeID", None)
                # Код агентства, запрашивающего финансирование для контракта.
                funding_requesting_agency_id = contract.get("content__award__purchaserInformation__fundingRequestingAgencyID", None)
                # Код офиса, запрашивающего финансирование для контракта.
                funding_requesting_office_id = contract.get("content__award__purchaserInformation__fundingRequestingOfficeID", None)
                # Описание типа действия по контракту.
                contract_action_type_description = contract.get("content__award__contractData__contractActionType__description", None)
                # Тип ценообразования.
                type_of_contract_pricing_description = contract.get("content__award__contractData__typeOfContractPricing__description", None)
                # Описание требований к контракту – цель и предмет закупки.
                description_of_contract_requirement = contract.get("content__award__contractData__descriptionOfContractRequirement", None)
                # Указывает, является ли контракт многолетним.
                multi_year_contract = contract.get("content__award__contractData__multiYearContract", None)
                # Указывает, является ли связанный IDV (Indefinite Delivery Vehicle) контрактом с одним или несколькими поставщиками.
                referenced_idv_multiple_or_single = contract.get("content__award__contractData__referencedIDVMultipleOrSingle", None)
                # Указывает тип IDV-контракта (Indefinite Delivery Vehicle).
                referenced_idv_type = contract.get("content__award__contractData__referencedIDVType", None)
                # Указывает, применяются ли к контракту требования по стандартам труда.
                labor_standards = contract.get("content__award__legislativeMandates__laborStandards", None)
                # Код, обозначающий тип продукции или услуги, предоставляемой по контракту.
                psc_code = contract.get("content__award__productOrServiceInformation__productOrServiceCode", None)
                # Определяет, относится ли контракт к категории "товары" (Product) или "услуги" (Service).
                psc_type = contract.get("content__award__productOrServiceInformation__productOrServiceCode__productOrServiceType", None)
                # Основной код отрасли по системе NAICS (North American Industry Classification System).
                naics_code = contract.get("content__award__productOrServiceInformation__principalNAICSCode", None)
                # Код страны происхождения товара или услуги.
                country_of_origin = contract.get("content__award__productOrServiceInformation__countryOfOrigin", None)
                # Официальное название поставщика, заключившего контракт.
                vendor_name = contract.get("content__award__vendor__vendorHeader__vendorName", None)
                # Указывает, относится ли компания к категории малого бизнеса.
                is_small_business = contract.get("content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isSmallBusiness", None)
                # Указывает, принадлежит ли компания ветерану с ограниченными возможностями, связанными со службой.
                is_veteran_owned_business = contract.get("content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isServiceRelatedDisabledVeteranOwnedBusiness", None)
                # Указывает, принадлежит ли компания женщине.
                is_women_owned = contract.get("content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isWomenOwned", None)
                # Указывает, является ли компания очень малым бизнесом.
                is_very_small_business = contract.get("content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isVerySmallBusiness", None)
                # Указывает, принадлежит ли компания малому бизнесу, управляемому женщиной.
                is_women_owned_small_business = contract.get("content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isWomenOwnedSmallBusiness", None)
                # Указывает, принадлежит ли компания экономически обездоленной женщине, владеющей малым бизнесом.
                is_economically_disadvantaged_women_owned_small_business = contract.get("content__award__vendor__vendorSiteDetails__vendorSocioEconomicIndicators__isEconomicallyDisadvantagedWomenOwnedSmallBusiness", None)
                # Указывает, является ли организация партнёрством или партнёрством с ограниченной ответственностью.
                is_partnership_or_limited_liability_partnership = contract.get("content__award__vendor__vendorSiteDetails__vendorBusinessTypes__businessOrOrganizationType__isPartnershipOrLimitedLiabilityPartnership", None)
                # Указывает, получает ли организация как контракты, так и гранты от федерального правительства.
                receives_contracts_and_grants = contract.get("content__award__vendor__vendorSiteDetails__vendorRelationshipWithFederalGovernment__receivesContractsAndGrants", None)
                # Указывает, является ли организация коммерческой, целью которой является получение прибыли.
                is_for_profit_organization = contract.get("content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__profitStructure__isForProfitOrganization", None)
                # Указывает штат, в котором зарегистрирована организация.
                vendor_state_of_incorporation = contract.get("content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__stateOfIncorporation", None)
                # Указывает страну, в которой зарегистрирована организация.
                vendor_country_of_incorporation = contract.get("content__award__vendor__vendorSiteDetails__vendorOrganizationFactors__countryOfIncorporation", None)
                # Улица, на которой расположена организация.
                vendor_location_street_address = contract.get("content__award__vendor__vendorSiteDetails__vendorLocation__streetAddress", None)
                # Город, в котором расположена организация.
                vendor_location_city = contract.get("content__award__vendor__vendorSiteDetails__vendorLocation__city", None)
                # Код штата, в котором расположена организация.
                vendor_location_state = contract.get("content__award__vendor__vendorSiteDetails__vendorLocation__state", None)
                # Город, соответствующий почтовому индексу.
                vendor_location_zipcode = contract.get("content__award__vendor__vendorSiteDetails__vendorLocation__ZIPCode", None)
                # Код страны, в которой расположена организация.
                vendor_location_country = contract.get("content__award__vendor__vendorSiteDetails__vendorLocation__countryCode", None)
                # Уникальный идентификатор организации (UEI), используемый для официальной идентификации.
                vendor_uei = contract.get("content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__UEI", None)
                # UEI основного (родительского) бизнеса или организации, которая является владельцем или управляющим.
                vendor_ultimate_parent_uei = contract.get("content__award__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__ultimateParentUEI", None)
                # CAGE (Commercial and Government Entity) код, присвоенный организации для государственных контрактов.
                vendor_cage_code = contract.get("content__award__vendor__vendorSiteDetails__entityIdentifiers__cageCode", None)
                # Дата регистрации организации в CCR.
                vendor_registration_date = contract.get("content__award__vendor__vendorSiteDetails__ccrRegistrationDetails__registrationDate", None)
                # Дата продления регистрации организации в CCR.
                vendor_renewal_date = contract.get("content__award__vendor__vendorSiteDetails__ccrRegistrationDetails__renewalDate", None)
                # Оценка размера бизнеса, произведённая контрактующим офицером.
                vendor_size = contract.get("content__award__vendor__contractingOfficerBusinessSizeDetermination", None)
                # Код штата, в котором выполняется контракт.
                place_of_performance_state = contract.get("content__award__placeOfPerformance__principalPlaceOfPerformance__stateCode", None)
                # Код страны, в которой выполняется контракт.
                place_of_performance_country = contract.get("content__award__placeOfPerformance__principalPlaceOfPerformance__countryCode", None)
                # Почтовый индекс места исполнения контракта.
                place_of_performance_zip = contract.get("content__award__placeOfPerformance__placeOfPerformanceZIPCode", None)
                # Уровень конкуренции по контракту.
                competition_extent_competed = contract.get("content__award__competition__extentCompeted", None)
                # Процедура подачи предложений для контракта.
                competition_solicitation_procedures = contract.get("content__award__competition__solicitationProcedures", None)
                # Причина, по которой контракт не был конкурентным.
                competition_reason_not_competed = contract.get("content__award__competition__reasonNotCompeted", None)
                # !!!!!!!
                competition_number_of_offers_received = int(contract.get("content__award__competition__numberOfOffersReceived", 0) or 0)
                # Количество предложений, полученных для контракта.
                competition_idv_number_of_offers_received = int(contract.get("content__award__competition__idvNumberOfOffersReceived", 0) or 0)
                # Указывает, были ли сделаны публичные объявления о федеральных бизнес-возможностях (Federal Business Opportunities).
                competition_fed_biz_opps = contract.get("content__award__competition__fedBizOpps", None)
                # Статус транзакции.
                award_transaction_information_status = contract.get("content__award__transactionInformation__status", None)

                

            elif contract.get("contract_type") == "IDV":
                contract_type = contract.get("contract_type", None)
                piid = contract.get("content__award__awardID__awardContractID__PIID", None)
                idv_piid = contract.get("content__IDV__contractID__IDVID__PIID", None)
                referenced_piid = contract.get("content__award__awardID__referencedIDVID__PIID", None)
                mod_number = contract.get("content__IDV__contractID__IDVID__modNumber", None)

                signed_date = contract.get("content__IDV__relevantContractDates__signedDate", None)
                effective_date = contract.get("content__IDV__relevantContractDates__effectiveDate", None)
                # Окончательная дата завершения контракта, учитывая все возможные продления.
                ultimate_completion_date = contract.get("content__IDV__relevantContractDates__lastDateToOrder", None)
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
            
            elif contract.get("contract_type") == "OTHERTRANSACTIONAWARD":
                contract_type = contract.get("contract_type", None)
                piid = contract.get("content__OtherTransactionAward__OtherTransactionAwardID__OtherTransactionAwardContractID__PIID", None)
                idv_piid = contract.get("content__OtherTransactionAward__OtherTransactionAwardID__referencedIDVID__PIID", None)
                referenced_piid = contract.get("content__OtherTransactionAward__OtherTransactionAwardID__referencedIDVID__PIID", None)
                mod_number = contract.get("content__OtherTransactionAward__OtherTransactionAwardID__OtherTransactionAwardContractID__modNumber", None)

                signed_date = contract.get("content__OtherTransactionAward__contractDetail__relevantContractDates__signedDate", None)
                effective_date = contract.get("content__OtherTransactionAward__contractDetail__relevantContractDates__effectiveDate", None)
                # Окончательная дата завершения контракта, учитывая все возможные продления.
                ultimate_completion_date = contract.get("content__OtherTransactionAward__contractDetail__relevantContractDates__currentCompletionDate", None)
                obligated_amount = float(contract.get("content__OtherTransactionAward__contractDetail__dollarValues__obligatedAmount", 0) or 0)
                base_and_exercised_options_value = float(contract.get("content__OtherTransactionAward__contractDetail__dollarValues__baseAndExercisedOptionsValue", 0) or 0)
                base_and_all_options_value = float(contract.get("content__OtherTransactionAward__contractDetail__dollarValues__baseAndAllOptionsValue", 0) or 0)
                vendor_uei = contract.get("content__OtherTransactionAward__contractDetail__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__UEI", None)
                naics_code = None  # do not have it
                psc_code = contract.get("content__OtherTransactionAward__contractDetail__PSCCode", None)
                contracting_office_agency_id = contract.get("content__OtherTransactionAward__contractDetail__purchaserInformation__contractingOfficeAgencyID", None)
                contracting_office_id = contract.get("content__OtherTransactionAward__contractDetail__purchaserInformation__contractingOfficeID", None)
                funding_requesting_agency_id = contract.get("content__OtherTransactionAward__contractDetail__purchaserInformation__fundingRequestingAgencyID", None)
                funding_requesting_office_id = contract.get("content__OtherTransactionAward__contractDetail__purchaserInformation__fundingRequestingOfficeID", None)
                number_of_offers_received = None # do not have it
                extent_competed = contract.get("content__OtherTransactionAward__contractDetail__competition__extentCompeted", None)

            elif contract.get("contract_type") == "OTHERTRANSACTIONIDV":
                contract_type = contract.get("contract_type", None)
                piid = contract.get("content__OtherTransactionIDV__OtherTransactionIDVID__OtherTransactionIDVContractID__PIID", None)
                idv_piid = contract.get("content__OtherTransactionIDV__OtherTransactionIDVID__OtherTransactionIDVContractID__PIID", None)
                referenced_piid = None  # do not have it
                mod_number = contract.get("content__OtherTransactionIDV__OtherTransactionIDVID__OtherTransactionIDVContractID__modNumber", None)
   
                signed_date = contract.get("content__OtherTransactionIDV__contractDetail__relevantContractDates__signedDate", None)
                effective_date = contract.get("content__OtherTransactionIDV__contractDetail__relevantContractDates__effectiveDate", None)
                # Окончательная дата завершения контракта, учитывая все возможные продления.
                ultimate_completion_date = contract.get("content__OtherTransactionIDV__contractDetail__relevantContractDates__currentCompletionDate", None)
                obligated_amount = float(contract.get("content__OtherTransactionIDV__contractDetail__dollarValues__obligatedAmount", 0) or 0)
                base_and_exercised_options_value = float(contract.get("content__OtherTransactionIDV__contractDetail__dollarValues__baseAndExercisedOptionsValue", 0) or 0)
                base_and_all_options_value = float(contract.get("content__OtherTransactionIDV__contractDetail__dollarValues__baseAndAllOptionsValue", 0) or 0)
                vendor_uei = contract.get("content__OtherTransactionIDV__contractDetail__vendor__vendorSiteDetails__entityIdentifiers__vendorUEIInformation__UEI", None)
                naics_code = None  # do not have it
                psc_code = contract.get("content__OtherTransactionIDV__contractDetail__PSCCode", None)
                contracting_office_agency_id = contract.get("content__OtherTransactionIDV__contractDetail__purchaserInformation__contractingOfficeAgencyID", None)
                contracting_office_id = contract.get("content__OtherTransactionIDV__contractDetail__purchaserInformation__contractingOfficeID", None)
                funding_requesting_agency_id = contract.get("content__OtherTransactionIDV__contractDetail__purchaserInformation__fundingRequestingAgencyID", None)
                funding_requesting_office_id = contract.get("content__OtherTransactionIDV__contractDetail__purchaserInformation__fundingRequestingOfficeID", None)
                number_of_offers_received = None  # do not have it
                extent_competed = contract.get("content__OtherTransactionIDV__contractDetail__competition__extentCompeted", None)
                
            else:
                # Form a file name in the format errors_year_month_day.log
                error_log_path = f"errors_{datetime.now().strftime('%Y_%m_%d')}.log"
                error_message = f"{datetime.now().isoformat()} - ⚠️ Unknown contract type: {json.dumps(contract, indent=2, ensure_ascii=False)}\n"
                 # Write the error to the log file
                with open(error_log_path, "a", encoding="utf-8") as error_log:
                    error_log.write(error_message)

                continue

            # Preparing data for insertion into the DB
            contract_data = (
                contract_type,
                modified,
                agency_id,
                piid,
                mod_number,
                idv_piid,
                referenced_piid,
                signed_date,
                effective_date,
                ultimate_completion_date,
                obligated_amount,
                base_and_all_options_value,
                total_obligated_amount,
                total_base_and_all_options_value,
                contracting_office_agency_id,
                contracting_office_id,
                funding_requesting_agency_id,
                funding_requesting_office_id,
                contract_action_type_description,
                type_of_contract_pricing_description,
                description_of_contract_requirement,
                multi_year_contract,
                referenced_idv_multiple_or_single,
                referenced_idv_type,
                labor_standards,
                psc_code,
                psc_type,
                naics_code,
                country_of_origin,
                vendor_name,
                is_small_business,
                is_veteran_owned_business,
                is_women_owned,
                is_very_small_business,
                is_women_owned_small_business,
                is_economically_disadvantaged_women_owned_small_business,
                is_partnership_or_limited_liability_partnership,
                receives_contracts_and_grants,
                is_for_profit_organization,
                vendor_state_of_incorporation,
                vendor_country_of_incorporation,
                vendor_location_street_address,
                vendor_location_city,
                vendor_location_state,
                vendor_location_zipcode,
                vendor_location_country,
                vendor_uei,
                vendor_ultimate_parent_uei,
                vendor_cage_code,
                vendor_registration_date,
                vendor_renewal_date,
                vendor_size,
                place_of_performance_state,
                place_of_performance_country,
                place_of_performance_zip,
                competition_extent_competed,
                competition_solicitation_procedures,
                competition_reason_not_competed,
                competition_number_of_offers_received,
                competition_idv_number_of_offers_received,
                competition_fed_biz_opps,
                award_transaction_information_status,
                str(Path(file_path).with_suffix(".parquet"))
            )

            # Insert into DB
            try:
                cursor.executemany("""
                    INSERT INTO contracts (
                        contract_type,
                        modified,
                        agency_id,
                        piid,
                        mod_number,
                        idv_piid,
                        referenced_piid,
                        signed_date,
                        effective_date,
                        ultimate_completion_date,
                        obligated_amount,
                        base_and_all_options_value,
                        total_obligated_amount,
                        total_base_and_all_options_value,
                        contracting_office_agency_id,
                        contracting_office_id,
                        funding_requesting_agency_id,
                        funding_requesting_office_id,
                        contract_action_type_description,
                        type_of_contract_pricing_description,
                        description_of_contract_requirement,
                        multi_year_contract,
                        referenced_idv_multiple_or_single,
                        referenced_idv_type,
                        labor_standards,
                        psc_code,
                        psc_type,
                        naics_code,
                        country_of_origin,
                        vendor_name,
                        is_small_business,
                        is_veteran_owned_business,
                        is_women_owned,
                        is_very_small_business,
                        is_women_owned_small_business,
                        is_economically_disadvantaged_women_owned_small_business,
                        is_partnership_or_limited_liability_partnership,
                        receives_contracts_and_grants,
                        is_for_profit_organization,
                        vendor_state_of_incorporation,
                        vendor_country_of_incorporation,
                        vendor_location_street_address,
                        vendor_location_city,
                        vendor_location_state,
                        vendor_location_zipcode,
                        vendor_location_country,
                        vendor_uei,
                        vendor_ultimate_parent_uei,
                        vendor_cage_code,
                        vendor_registration_date,
                        vendor_renewal_date,
                        vendor_size,
                        place_of_performance_state,
                        place_of_performance_country,
                        place_of_performance_zip,
                        competition_extent_competed,
                        competition_solicitation_procedures,
                        competition_reason_not_competed,
                        competition_number_of_offers_received,
                        competition_idv_number_of_offers_received,
                        competition_fed_biz_opps,
                        award_transaction_information_status
                        file_path, 
                        created_at, 
                        updated_at
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, NOW(), NOW()
                    )
                """ , [contract_data])

            except Exception as e:
                click.echo(f"❌ Error inserting contract {piid}: {str(e)}")

        conn.commit()
        click.echo(f"📄 Successfully saved {saved_count} contracts out of {len(contracts)}")

        # Remove original JSON file
        # os.remove(file_path)
        # click.echo(f"🗑 Deleted JSON file: {file_path}")

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