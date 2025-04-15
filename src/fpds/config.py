"""
Configurations and constants

author: derek663@gmail.com
last_updated: 12/27/2022
"""
import os
import json
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

HOME = Path.home()
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")

# FPDS-specific configurations
FPDS_DATA_DIR = HOME / ".fpds"
FPDS_FIELDS_FILE = "fields.json"

# assumes a python3.x version
if sys.version_info[1] <= 8:
    from importlib.resources import path

    with path("fpds.constants", FPDS_FIELDS_FILE) as file:  # type: ignore
        FPDS_FIELDS_FILE_PATH = file
else:
    from importlib.resources import files

    FPDS_FIELDS_FILE_PATH = files("fpds.constants").joinpath(FPDS_FIELDS_FILE)

# location where downloaded data will be dumped
FPDS_DATA_DATE_DIR = FPDS_DATA_DIR / CURRENT_DATE

# actions
FPDS_DATA_DATE_DIR.mkdir(parents=True, exist_ok=True)

with Path(FPDS_FIELDS_FILE_PATH).open(encoding="utf-8") as file:  # type: ignore
    FPDS_FIELDS_CONFIG = json.load(file)

# ===============================
# 🚀 DATABASE CONFIG FROM `.env`
# ===============================
load_dotenv()
DB_TYPE = os.getenv("DB_TYPE", "mysql")  # mysql, postgresql, sqlite и т. д.
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "fpds")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")

# SQLAlchemy URL
if DB_TYPE == "sqlite":
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_NAME}.db"
elif DB_TYPE == "mysql":
    SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
elif DB_TYPE == "postgresql":
    SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
else:
    raise ValueError(f"❌ Неподдерживаемый тип БД: {DB_TYPE}")

# DB_CONFIG для обычного подключения (например, `mysql.connector`)
DB_CONFIG = {
    "host": DB_HOST,
    "port": int(DB_PORT),
    "user": DB_USER,
    "password": DB_PASSWORD,
    "database": DB_NAME,
}