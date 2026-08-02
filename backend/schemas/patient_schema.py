from pydantic import BaseModel
from typing import Optional


class PatientBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    phone: str
    email: str
    address: str


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True