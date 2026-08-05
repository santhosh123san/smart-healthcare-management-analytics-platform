from sqlalchemy.orm import Session
from backend.models.patient import Patient
from backend.schemas.patient_schema import PatientCreate


def get_all_patients(db: Session):
    return db.query(Patient).all()


def get_patient_by_id(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.patient_id == patient_id).first()


def create_patient(db: Session, patient: PatientCreate):
    new_patient = Patient(
        first_name=patient.first_name,
        last_name=patient.last_name,
        gender=patient.gender,
        date_of_birth=patient.date_of_birth,
        phone=patient.phone,
        email=patient.email,
        blood_group=patient.blood_group,
        address=patient.address,
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient