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


def update_patient(db: Session, patient_id: int, patient_data: PatientCreate):
    patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()

    if patient:
        for key, value in patient_data.model_dump().items():
            setattr(patient, key, value)

        db.commit()
        db.refresh(patient)

    return patient


def delete_patient(db: Session, patient_id: int):
    patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()

    if patient:
        db.delete(patient)
        db.commit()

    return patient