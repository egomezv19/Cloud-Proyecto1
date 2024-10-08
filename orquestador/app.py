from flask import Flask, jsonify
from services import get_empresas, get_empleos, get_pagos, get_alojamientos
from urllib.parse import quote as url_quote

app = Flask(__name__)


@app.route('/empresas', methods=['GET'])
def empresas():
    try:
        empresas_data = get_empresas()
        return jsonify(empresas_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/empleos', methods=['GET'])
def empleos():
    try:
        empleos_data = get_empleos()
        return jsonify(empleos_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/pagos', methods=['GET'])
def pagos():
    try:
        pagos_data = get_pagos()
        return jsonify(pagos_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/alojamientos', methods=['GET']) 
def alojamiento():
    try:
        alojamiento_data = get_alojamientos()
        return jsonify(alojamiento_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Mantiene el puerto 5000 para la exposición
