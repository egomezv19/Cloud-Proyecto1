from flask import Blueprint, jsonify
from services import call_microservices

# Definir un blueprint para el orquestador
orchestrator_blueprint = Blueprint('orchestrator', __name__)

# Ruta para orquestar las llamadas a otros microservicios
@orchestrator_blueprint.route('/orquestador', methods=['GET'])
def orchestrate():
    try:
        # Llamar a los microservicios y combinar las respuestas
        combined_response = call_microservices()
        return jsonify(combined_response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
