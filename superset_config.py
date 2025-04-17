import os
from superset.config import *

SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "my-saf3-secret-key-here-12345!")
