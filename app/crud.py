from sqlalchemy.orm import Session
from . import models, schemas

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Patient).offset(skip).limit(limit).all()
