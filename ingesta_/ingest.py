import pandas as pd
import mysql.connector
import boto3

# Conectar a la base de datos MySQL
conn = mysql.connector.connect(
    host="db_mysql",
    user="root",
    password="nosejajaja123-",
    database="microservicio2_db"
)

# Consulta SQL
query = "SELECT * FROM Empleo"
df = pd.read_sql(query, conn)

# Guardar los datos en un archivo CSV
csv_file = '/app/empleos_data.csv'
df.to_csv(csv_file, index=False)

# Cargar el archivo CSV a un bucket de S3
s3 = boto3.client('s3')
bucket_name = 'your-s3-bucket-name'
s3.upload_file(csv_file, bucket_name, 'empleos_data.csv')
