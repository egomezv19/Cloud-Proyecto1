from flask import Flask
from routes import orchestrator_blueprint

app = Flask(__name__)

# Registro de las rutas (endpoints)
app.register_blueprint(orchestrator_blueprint)

if __name__ == '__main__':
    # Ejecuta la aplicación Flask
    app.run(host='0.0.0.0', port=5000)
