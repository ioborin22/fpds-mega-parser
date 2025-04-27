import ssl
import certifi
from urllib.request import urlopen

url = "https://www.fpds.gov/ezsearch/FEEDS/ATOM?s=FPDS&FEEDNAME=PUBLIC&q=SIGNED_DATE:[2023/01/01,2023/01/01]"

try:
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    with urlopen(url, context=ssl_context) as response:
        print("✅ SUCCESS:", response.status)
        print(response.read()[:500])  # первые 500 байт
except Exception as e:
    print("❌ ERROR:", e)
