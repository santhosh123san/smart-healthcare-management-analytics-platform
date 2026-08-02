from sqlalchemy.orm import Session
from backend.schemas.patient_schema import PatientCreate
from backend.services.patient_service import (
    get_all_patients,
    create_patient
)


def fetch_patients(db: Session):
    return get_all_patients(db)


def add_patient(patient: PatientCreate, db: Session):
    return create_patient(db, patient)