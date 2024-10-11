FROM python:3.8-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script de ingesta
COPY ingest_mongodb.py .

# Copiar la carpeta de datos (para insertar)
COPY data/ ./data/

# Comando para ejecutar el script de ingesta
ENTRYPOINT ["python", "ingest_mongodb.py"]
