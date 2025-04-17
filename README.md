pip install -r requirements.txt

source venv/bin/activate

Установи переменные окружения:

py -3.11 -m venv venv 
.\venv\Scripts\activate
$env:FLASK_APP="superset"
$env:SUPERSET_CONFIG_PATH = "C:\Users\win11\Projects\fpds\superset_config.py"