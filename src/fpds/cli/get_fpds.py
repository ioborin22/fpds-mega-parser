# fpds/cli/get_fpds.py

import click
import asyncio
import json
from pathlib import Path
from itertools import chain
from fpds import fpdsRequest


@click.command()
@click.argument("date")
@click.option("-o", "--output", required=False, help="Output directory")
def get_fpds(date, output):
    """Download FPDS data for a specific date."""
    try:
        year, month, day = date.split("/")
    except ValueError:
        click.echo(
            f"⚠️ Invalid date format: {date}. Expected format: YYYY/MM/DD")
        return

    data_dir = Path(output) if output else Path("/Users/iliaoborin/fpds/data/")
    data_file = data_dir / year / f"{month}_{day}.json"

    formatted_date = f"SIGNED_DATE=[{date},{date}]"
    params = dict([formatted_date.split("=")])

    click.echo(f"🌐 Downloading FPDS data for {date}...")

    request = fpdsRequest(**params, cli_run=True)

    try:
        data = asyncio.run(request.data())
        records = list(chain.from_iterable(data))

        data_file.parent.mkdir(parents=True, exist_ok=True)

        with open(data_file, "w") as outfile:
            json.dump(records, outfile, indent=4)

        click.echo(f"✅ Saved {len(records)} records to {data_file}")

        if not records:
            click.echo("⚠️ No records found. The file is empty.")

    except Exception as e:
        click.echo(f"❌ Error occurred: {e}")
