import os
import json
import pandas as pd
from pymongo import MongoClient
import boto3

# Conexión a MongoDB
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['universidad']
collection_pagos = db['pagos']
collection_alojamientos = db['alojamientos']


with open('/app/data/pagos_data.json') as f:
    pagos_data = json.load(f)
    collection_pagos.insert_many(pagos_data)

with open('/app/data/alojamientos_data.json') as f:
    alojamientos_data = json.load(f)
    collection_alojamientos.insert_many(alojamientos_data)

print("Inserción de datos completa.")


pagos = list(collection_pagos.find())
alojamientos = list(collection_alojamientos.find())


df_pagos = pd.DataFrame(pagos)
df_alojamientos = pd.DataFrame(alojamientos)


if '_id' in df_pagos.columns:
    df_pagos = df_pagos.drop('_id', axis=1)
if '_id' in df_alojamientos.columns:
    df_alojamientos = df_alojamientos.drop('_id', axis=1)

csv_file_pagos = '/tmp/pagos_data.csv'
csv_file_alojamientos = '/tmp/alojamientos_data.csv'
df_pagos.to_csv(csv_file_pagos, index=False)
df_alojamientos.to_csv(csv_file_alojamientos, index=False)

# Subir los archivos a S3
s3 = boto3.client('s3')
bucket_name = os.getenv('AWS_S3_BUCKET_NAME')

s3.upload_file(csv_file_pagos, bucket_name, 'pagos_data.csv')
s3.upload_file(csv_file_alojamientos, bucket_name, 'alojamientos_data.csv')

print("Ingesta completa y archivos subidos a S3")
    