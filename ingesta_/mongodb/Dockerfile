FROM python:3.8-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script de ingesta
COPY ingest_mongodb.py .

# Copiar la carpeta de datos (para insertar)
COPY ./data/pagos_data.json /app/data/pagos_data.json
COPY ./data/alojamientos_data.json /app/data/alojamientos_data.json

# Comando para ejecutar el script de ingesta
ENTRYPOINT ["python", "ingest_mongodb.py"]
