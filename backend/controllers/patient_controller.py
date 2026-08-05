from sqlalchemy.orm import Session
from backend.schemas.patient_schema import PatientCreate
from backend.services.patient_service import (
    get_all_patients,
    get_patient_by_id,
    create_patient
)


def get_patients_controller(db: Session):
    return get_all_patients(db)


def get_patient_controller(patient_id: int, db: Session):
    return get_patient_by_id(db, patient_id)


def create_patient_controller(patient: PatientCreate, db: Session):
    return create_patient(db, patient)