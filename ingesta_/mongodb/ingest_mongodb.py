import os
import pandas as pd
from pymongo import MongoClient
import boto3

# Conexión a MongoDB
MONGODB_URI = 'mongodb://mongodb:27017/universidad'  # URI de MongoDB
client = MongoClient(MONGODB_URI)
db = client['universidad']  # Nombre de la base de datos
collection = db['pagos']  # Nombre de la colección

# Extracción de datos desde MongoDB
data = list(collection.find())
df = pd.DataFrame(data)

# Eliminamos la columna '_id' ya que no es necesario en el CSV/JSON
if '_id' in df.columns:
    df = df.drop('_id', axis=1)

# Guardar los datos en un archivo CSV
csv_file = '/app/data/pagos_data.csv'
df.to_csv(csv_file, index=False)

# También puedes guardarlo en un archivo JSON si lo prefieres
json_file = '/app/data/pagos_data.json'
df.to_json(json_file, orient='records')

# Cargar el archivo CSV y JSON a un bucket de S3
s3 = boto3.client('s3')
bucket_name = 'ingesta1'  # Nombre del bucket de S3
s3.upload_file(csv_file, bucket_name, 'pagos_data.csv')
s3.upload_file(json_file, bucket_name, 'pagos_data.json')

print("Ingesta de MongoDB completa y archivos subidos a S3.")
