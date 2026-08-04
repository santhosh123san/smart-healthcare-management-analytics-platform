from sqlalchemy.orm import Session
from backend.models.doctor import Doctor
from backend.schemas.doctor_schema import DoctorCreate


def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def create_doctor(db: Session, doctor: DoctorCreate):
    new_doctor = Doctor(**doctor.model_dump())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor