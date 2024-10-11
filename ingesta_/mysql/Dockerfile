# Usamos una imagen base de Python
FROM python:3.8-slim

# Configuramos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt y lo instalamos
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos los archivos del microservicio necesarios para la ingesta
COPY ingest_mysql.py ./ingest_mysql.py

# Copiamos la carpeta vacía data para almacenar archivos procesados
COPY data/ ./data/

# Comando para ejecutar el script de ingesta
ENTRYPOINT ["python", "ingest_mysql.py"]
