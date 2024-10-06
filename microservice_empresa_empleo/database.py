from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:nosejajaja123-@localhost/microservicio2_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

try:
    db = SessionLocal()
    print("Conexión a la base de datos exitosa :)")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
finally:
    db.close()
