from sqlalchemy.orm import Session
from models import Empresa, Empleo
from schemas import EmpresaCreate, EmpresaUpdate, EmpresaDelete, EmpleoCreate, EmpleoUpdate, EmpleoDelete


# CRUD para Empresa
def create_empresa(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def get_empresa(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()

def get_empresas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Empresa).offset(skip).limit(limit).all()

def update_empresa(db: Session, empresa_id: int, empresa: schemas.EmpresaUpdate):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()
    if db_empresa:
        empresa_data = empresa.dict(exclude_unset=True)  # Actualiza solo los campos proporcionados
        for key, value in empresa_data.items():
            setattr(db_empresa, key, value)
        db.commit()
        db.refresh(db_empresa)
        return db_empresa
    return None

def delete_empresa(db: Session, empresa: schemas.EmpresaDelete):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa.id).first()
    if db_empresa:
        db.delete(db_empresa)
        db.commit()
        return db_empresa
    return None

# CRUD para Empleo
def create_empleo(db: Session, empleo: schemas.EmpleoCreate):
    db_empleo = models.Empleo(**empleo.dict())
    db.add(db_empleo)
    db.commit()
    db.refresh(db_empleo)
    return db_empleo

def get_empleo(db: Session, empleo_id: int):
    return db.query(models.Empleo).filter(models.Empleo.id_empleo == empleo_id).first()

def get_empleos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Empleo).offset(skip).limit(limit).all()

def update_empleo(db: Session, empleo_id: int, empleo: schemas.EmpleoUpdate):
    db_empleo = db.query(models.Empleo).filter(models.Empleo.id_empleo == empleo_id).first()
    if db_empleo:
        empleo_data = empleo.dict(exclude_unset=True)  # Actualiza solo los campos proporcionados
        for key, value in empleo_data.items():
            setattr(db_empleo, key, value)
        db.commit()
        db.refresh(db_empleo)
        return db_empleo
    return None

def delete_empleo(db: Session, empleo: schemas.EmpleoDelete):
    db_empleo = db.query(models.Empleo).filter(models.Empleo.id_empleo == empleo.id).first()
    if db_empleo:
        db.delete(db_empleo)
        db.commit()
        return db_empleo
    return None
