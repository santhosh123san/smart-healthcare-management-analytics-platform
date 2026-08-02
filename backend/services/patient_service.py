from sqlalchemy.orm import Session
from backend.models.patient import Patient
from backend.schemas.patient_schema import PatientCreate


def get_all_patients(db: Session):
    return db.query(Patient).all()


def create_patient(db: Session, patient: PatientCreate):
    new_patient = Patient(**patient.model_dump())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient