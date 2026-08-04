from sqlalchemy.orm import Session
from backend.schemas.doctor_schema import DoctorCreate
from backend.services.doctor_service import (
    get_all_doctors,
    create_doctor
)


def fetch_doctors(db: Session):
    return get_all_doctors(db)


def add_doctor(doctor: DoctorCreate, db: Session):
    return create_doctor(db, doctor)