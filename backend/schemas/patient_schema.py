from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class PatientBase(BaseModel):
    first_name: str
    last_name: str
    gender: str
    date_of_birth: date
    phone: str
    email: EmailStr
    blood_group: str
    address: str


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    patient_id: int

    class Config:
        from_attributes = True