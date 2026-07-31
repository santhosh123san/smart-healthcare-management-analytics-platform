from sqlalchemy import Column, Integer, String
from backend.database.db import Base

class Doctor(Base):
    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    specialization = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))