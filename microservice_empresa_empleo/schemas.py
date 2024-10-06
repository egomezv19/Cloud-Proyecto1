from pydantic import BaseModel
from typing import Optional

class EmpresaBase(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None

    class Config:
        from_attributes = True

class EmpresaCreate(BaseModel):
    nombre: str
    direccion: str
    telefono: Optional[str] = None
    email: Optional[str] = None

    class Config:
        from_attributes = True

class EmpresaUpdate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id_empresa: int

    class Config:
        from_attributes = True

class EmpleoBase(BaseModel):
    id_empresa: Optional[int] = None
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    requisitos: Optional[str] = None
    salario: Optional[float] = None

    class Config:
        from_attributes = True

class EmpleoCreate(BaseModel):
    id_empresa: int
    titulo: str
    descripcion: str
    requisitos: Optional[str] = None
    salario: float

    class Config:
        from_attributes = True

class EmpleoUpdate(EmpleoBase):
    pass

class Empleo(EmpleoBase):
    id_empleo: int

    class Config:
        from_attributes = True
