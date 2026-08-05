from sqlalchemy import Column, Integer, String, Date
from backend.database.db import Base

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(String(10))
    date_of_birth = Column(Date)
    phone = Column(String(15))
    email = Column(String(100))
    blood_group = Column(String(10))
    address = Column(String(255))