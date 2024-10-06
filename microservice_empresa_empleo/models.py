from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "Empresa"  
    id_empresa = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(Text, nullable=False)
    telefono = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)
    empleos = relationship("Empleo", back_populates="empresa")

class Empleo(Base):
    __tablename__ = "Empleo"  
    id_empleo = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(Integer, ForeignKey('Empresa.id_empresa'))     
    titulo = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    requisitos = Column(Text, nullable=True)
    salario = Column(Integer, nullable=False)

    empresa = relationship("Empresa", back_populates="empleos")
