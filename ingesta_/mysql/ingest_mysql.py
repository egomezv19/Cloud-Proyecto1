import pandas as pd
import mysql.connector
import boto3
from pymongo import MongoClient

# Conectar a la base de datos MySQL
conn_mysql = mysql.connector.connect(
    host="db_mysql",
    user="root",
    password="nosejajaja123-",
    database="microservicio2_db"
)

# Conectar a la base de datos MongoDB
mongo_client = MongoClient('mongodb://db_mongo:27017/')
mongo_db = mongo_client['universidad']
mongo_collection = mongo_db['Alojamientos']

# Consulta SQL para MySQL
query_mysql = "SELECT * FROM Empleo"
df_mysql = pd.read_sql(query_mysql, conn_mysql)

# Guardar los datos en un archivo CSV desde MySQL
csv_file_mysql = '/app/empleos_data.csv'
df_mysql.to_csv(csv_file_mysql, index=False)

# Consulta para MongoDB y convertir a DataFrame
mongo_data = list(mongo_collection.find())
df_mongo = pd.DataFrame(mongo_data)

# Guardar los datos en un archivo CSV desde MongoDB
csv_file_mongo = '/app/alojamientos_data.csv'
df_mongo.to_csv(csv_file_mongo, index=False)

# Configurar el cliente S3
s3 = boto3.client('s3')
bucket_name = 'your-s3-bucket-name'

# Subir archivos CSV a S3
s3.upload_file(csv_file_mysql, bucket_name, 'empleos_data.csv')
s3.upload_file(csv_file_mongo, bucket_name, 'alojamientos_data.csv')

# Cerrar las conexiones
conn_mysql.close()
mongo_client.close()
