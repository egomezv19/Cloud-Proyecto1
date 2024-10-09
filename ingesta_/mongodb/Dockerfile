# Usamos una imagen base de Python
FROM python:3.8-slim

# Configuramos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt y lo instalamos
COPY mongodb/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el archivo de ingesta específico para MongoDB
COPY mongodb/ingest_mongodb.py ./ingest_mongodb.py

# Copiamos el archivo .env (asegúrate de que exista en el mismo directorio)
COPY mongodb/.env .env

# Copiamos el directorio de data (si tienes datos que necesitas dentro del contenedor)
COPY mongodb/data/ ./data/

# Comando para ejecutar el script de ingesta
ENTRYPOINT ["python", "ingest_mongodb.py"]
