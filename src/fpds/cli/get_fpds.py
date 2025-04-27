# fpds/cli/get_fpds.py

import click
import asyncio
import json
from pathlib import Path
from itertools import chain
from fpds import fpdsRequest
from datetime import datetime

@click.command()
@click.argument("date")
@click.option("-o", "--output", required=False, help="Output directory")
def get_fpds(date, output):
    """Download FPDS data for a specific date.
    - fpds get YYYY/MM/DD [OPTIONS]
    """    
    try:
        year, month, day = date.split("/")
    except ValueError:
        click.echo(
            f"⚠️ Invalid date format: {date}. Expected format: YYYY/MM/DD")
        return

    data_dir = Path(output) if output else Path(r"C:/Users/iobor/Projects/fpds/data")
    data_file = data_dir / year / f"{month}_{day}.json"

    formatted_date = f"SIGNED_DATE=[{date},{date}]"
    params = dict([formatted_date.split("=")])

    click.echo(f"🌐 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Downloading FPDS data for {date}...")

    request = fpdsRequest(**params, cli_run=True)

    try:
        data = asyncio.run(request.data())
        records = list(chain.from_iterable(data))

        data_file.parent.mkdir(parents=True, exist_ok=True)

        with open(data_file, "w") as outfile:
            json.dump(records, outfile, indent=4)

        click.echo(f"💾 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Saved {len(records)} records to {data_file}")

        if not records:
            click.echo("⚠️ No records found. The file is empty.")

    except Exception as e:
        click.echo(f"❌ Error occurred: {e}")
    
        # 👇 короткий update прямо тут
        try:
            import mysql.connector
            from fpds.config import DB_CONFIG

            db_conn = mysql.connector.connect(**DB_CONFIG)
            cursor = db_conn.cursor()

            date_sql = date.replace("/", "-")

            update_query = """
                UPDATE signed_date_records
                SET fpds_respond = %s
                WHERE signed_date = %s
            """
            cursor.execute(update_query, (str(e), date_sql))
            db_conn.commit()
            cursor.close()
            db_conn.close()

            click.echo(f"✅ Обновлено fpds_respond для {date_sql}")

        except Exception as db_error:
            click.echo(f"⚠️ Ошибка обновления fpds_respond: {db_error}")

