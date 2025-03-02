"""CLI namespace"""

import click

# Импорт команд для парсинга
from fpds.cli.parse_clickhouse import parse_clickhouse as _parse_clickhouse
from fpds.cli.parse_sql import parse_sql as _parse_sql


@click.group()
def cli():
    """
    CLI для парсинга данных FPDS.
    Доступные команды:
    - fpds parse clickhouse all
    - fpds parse clickhouse YYYY/MM/DD [OPTIONS]
    - fpds parse sql all
    - fpds parse sql YYYY/MM/DD [OPTIONS]
    """


@click.group()
def parse():
    """Группа команд `parse`"""


# Добавляем подкоманды
parse.add_command(_parse_clickhouse, name="clickhouse")
parse.add_command(_parse_sql, name="sql")

# Регистрируем команду `parse`
cli.add_command(parse)
