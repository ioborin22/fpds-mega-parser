from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Загрузка данных из файла Parquet
data = pd.read_parquet("/Users/iliaoborin/fpds/data/2011/09_09.parquet")

@app.route('/contracts', methods=['GET'])
def get_contracts():
    # Получаем piid из параметров запроса
    piid = request.args.get('piid')

    if not piid:
        return jsonify({"error": "PIID parameter is required"}), 400

    # Фильтрация данных по piid
    filtered_data = data[data['piid'] == piid]

    if filtered_data.empty:
        return jsonify({"message": "No contracts found for the given PIID"}), 404

    # Конвертация отфильтрованных данных в JSON
    result = filtered_data.to_dict(orient="records")

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)