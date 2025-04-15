import mysql.connector

config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "fpds"
}

try:
    conn = mysql.connector.connect(**config)
    print("✅ Успешное подключение к MySQL!")
    conn.close()
except mysql.connector.Error as e:
    print(f"❌ Ошибка подключения: {e}")
