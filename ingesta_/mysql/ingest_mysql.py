import os
import pandas as pd
import mysql.connector
import boto3

AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = 3306


conn = mysql.connector.connect(
    user="root", 
    password="nosejajaja123-",  
    host="db2",
    port=3306,  
    database="microservicio2_db"  
)


cursor = conn.cursor(dictionary=True)

query_empresas = "SELECT * FROM Empresa"
cursor.execute(query_empresas)
empresas = cursor.fetchall()

query_empleos = "SELECT * FROM Empleo"
cursor.execute(query_empleos)
empleos = cursor.fetchall()

df_empresas = pd.DataFrame(empresas)
df_empleos = pd.DataFrame(empleos)

csv_file_empresas = '/app/data/empresas_data.csv'
csv_file_empleos = '/app/data/empleos_data.csv'

df_empresas.to_csv(csv_file_empresas, index=False)
df_empleos.to_csv(csv_file_empleos, index=False)

# Conectar a S3 usando boto3
s3 = boto3.client('s3')

# Subir los archivos CSV al bucket
s3.upload_file(csv_file_empresas, AWS_S3_BUCKET_NAME, 'empresas_data.csv')
s3.upload_file(csv_file_empleos, AWS_S3_BUCKET_NAME, 'empleos_data.csv')

print("Ingesta de datos completada y archivos subidos a S3")

# Cerrar la conexión a la base de datos
cursor.close()
conn.close()
