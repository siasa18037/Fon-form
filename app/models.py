from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    allergies = Column(String)  # ยาที่แพ้
    diseases = Column(String)   # โรคประจำตัว
