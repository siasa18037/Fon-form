from pydantic import BaseModel

class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    weight: float
    height: float
    allergies: str
    diseases: str

class Patient(PatientCreate):
    id: int

    class Config:
        orm_mode = True
