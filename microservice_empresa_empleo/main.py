from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import crud
import httpx
from database import engine, SessionLocal 


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

MS1_URL = 'http://microservicio1:8080/programas'  


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/empresas/", response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.create_empresa(db=db, empresa=empresa)

@app.get("/empresas/{empresa_id}", response_model=schemas.Empresa)
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = crud.get_empresa(db, empresa_id=empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return db_empresa

@app.get("/empresas/", response_model=list[schemas.Empresa])
def read_empresas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_empresas(db, skip=skip, limit=limit)

@app.put("/empresas/{empresa_id}", response_model=schemas.Empresa)
def update_empresa(empresa_id: int, empresa: schemas.EmpresaUpdate, db: Session = Depends(get_db)):
    updated_empresa = crud.update_empresa(db, empresa_id=empresa_id, empresa=empresa)
    if updated_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return updated_empresa

@app.delete("/empresas/", response_model=schemas.Empresa)
def delete_empresa(empresa: schemas.EmpresaDelete, db: Session = Depends(get_db)):
    deleted_empresa = crud.delete_empresa(db, empresa=empresa)
    if deleted_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return deleted_empresa

# Endpoints para Empleo
@app.post("/empleos/", response_model=schemas.Empleo)
def create_empleo(empleo: schemas.EmpleoCreate, db: Session = Depends(get_db)):
    return crud.create_empleo(db=db, empleo=empleo)

@app.get("/empleos/{empleo_id}", response_model=schemas.Empleo)
def read_empleo(empleo_id: int, db: Session = Depends(get_db)):
    db_empleo = crud.get_empleo(db, empleo_id=empleo_id)
    if db_empleo is None:
        raise HTTPException(status_code=404, detail="Empleo no encontrado")
    return db_empleo

@app.get("/empleos/", response_model=list[schemas.Empleo])
def read_empleos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_empleos(db, skip=skip, limit=limit)

@app.put("/empleos/{empleo_id}", response_model=schemas.Empleo)
def update_empleo(empleo_id: int, empleo: schemas.EmpleoUpdate, db: Session = Depends(get_db)):
    updated_empleo = crud.update_empleo(db, empleo_id=empleo_id, empleo=empleo)
    if updated_empleo is None:
        raise HTTPException(status_code=404, detail="Empleo no encontrado")
    return updated_empleo

@app.delete("/empleos/", response_model=schemas.Empleo)
def delete_empleo(empleo: schemas.EmpleoDelete, db: Session = Depends(get_db)):
    deleted_empleo = crud.delete_empleo(db, empleo=empleo)
    if deleted_empleo is None:
        raise HTTPException(status_code=404, detail="Empleo no encontrado")
    return deleted_empleo



@app.get("/programas/", response_model=list[schemas.Programa])
async def get_programas():
    async with httpx.AsyncClient() as client:
        response = await client.get(MS1_URL)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="no se pudieron obtener los programas :c")
        return response.json()