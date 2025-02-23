from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port=8889,
            user='root',
            password='root',
            database='fpds'
        )
        print("Database connection established")
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection failed: {e}")
        return None

@app.route('/')
def test():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500
    else:
        conn.close()
        return jsonify({"success": "Connected to the database"}), 200
        

if __name__ == '__main__':
    app.run(debug=True)