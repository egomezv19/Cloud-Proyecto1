from pydantic import BaseModel
from typing import Optional


class EmpresaBase(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None

    class Config:
        orm_mode = True 


class EmpresaCreate(EmpresaBase):
    nombre: str
    direccion: str


class EmpresaUpdate(EmpresaBase):
    pass 


class Empresa(EmpresaBase):
    id_empresa: int


class EmpresaDelete(BaseModel):
    id_empresa: int



class EmpleoBase(BaseModel):
    id_empresa: Optional[int] = None
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    requisitos: Optional[str] = None
    salario: Optional[float] = None

    class Config:
        orm_mode = True  

class EmpleoCreate(EmpleoBase):
    id_empresa: int
    titulo: str
    descripcion: str
    salario: float

class EmpleoUpdate(EmpleoBase):
    pass  

class Empleo(EmpleoBase):
    id_empleo: int

class EmpleoDelete(BaseModel):
    id_empleo: int


class Programa(BaseModel):
    id: int
    nombre: str
    descripcion: str
    fecha_inicio: str
    fecha_final: str
