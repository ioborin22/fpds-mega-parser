"""CLI namespace"""

import click

# Импорт команд для парсинга
from fpds.cli.parse_clickhouse import parse_clickhouse as _parse_clickhouse
from fpds.cli.parse_sql import parse_sql as _parse_sql

# Импорт команды для скачивания одной даты
# <<< сюда импортируешь свою новую функцию
from fpds.cli.get_fpds import get_fpds as _get_fpds


@click.group()
def cli():
    """
    CLI для парсинга данных FPDS.
    Доступные команды:
    - fpds parse clickhouse all
    - fpds parse clickhouse YYYY/MM/DD [OPTIONS]
    - fpds parse sql all
    - fpds parse sql YYYY/MM/DD [OPTIONS]
    - fpds get YYYY/MM/DD [OPTIONS]
    """


@click.group()
def parse():
    """Группа команд `parse`"""


# Добавляем подкоманды в `parse`
parse.add_command(_parse_clickhouse, name="clickhouse")
parse.add_command(_parse_sql, name="sql")

# Регистрируем команду `parse`
cli.add_command(parse)

# 🚀 Добавляем команду `get`
cli.add_command(_get_fpds, name="get")
