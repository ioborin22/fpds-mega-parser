import os
from superset.config import *
import pymysql
pymysql.install_as_MySQLdb()

SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "my-saf3-secret-key-here-12345!")

APP_ICON = "/static/assets/images/my_logo.png"
FAVICON = "/static/assets/images/favicon.png" 
APP_NAME = "Procurelytics"