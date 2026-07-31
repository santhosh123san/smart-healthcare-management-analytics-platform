from sqlalchemy import Column, Integer, String, Date
from backend.database.db import Base

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(String(10))
    date_of_birth = Column(Date)
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(String(255))