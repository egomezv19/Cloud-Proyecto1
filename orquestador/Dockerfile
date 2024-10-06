# Usa una imagen ligera de Python
FROM python:3.9-alpine

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app
#xd
# Copia el archivo de dependencias y lo instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el código fuente dentro del contenedor
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
