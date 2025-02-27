"""CLI namespace"""

import click

from .parse import parse as _parse
from .parse import parse_clickhouse as _parse_clickhouse

@click.group()
def cli():
    """
    CLI for parsing the FPDS ATOM feed found at
    https://www.fpds.gov/fpdsng_cms/index.php/en/
    """


cli.add_command(_parse)
cli.add_command(_parse_clickhouse)