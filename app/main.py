from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware

# สร้างตารางในฐานข้อมูล SQLite
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # หรือเฉพาะ "http://localhost"
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db=db, patient=patient)

@app.get("/patients/", response_model=list[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_patients(db=db, skip=skip, limit=limit)
