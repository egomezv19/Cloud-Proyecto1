from flask import Flask, jsonify
from services import get_estudiantes, get_empresas, get_programas, get_pagos

app = Flask(__name__)


@app.route('/estudiantes', methods=['GET'])
def estudiantes():
    try:
        estudiantes_data = get_estudiantes()
        return jsonify(estudiantes_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/empresas', methods=['GET'])
def empresas():
    try:
        empresas_data = get_empresas()
        return jsonify(empresas_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/programas', methods=['GET'])
def programas():
    try:
        programas_data = get_programas()
        return jsonify(programas_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/pago', methods=['GET'])
def pagos():
    try:
        pagos_data = get_pagos()
        return jsonify(pagos_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  
