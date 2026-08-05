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


def update_doctor(db: Session, doctor_id: int, doctor_data: DoctorCreate):
    doctor = db.query(Doctor).filter(Doctor.doctor_id == doctor_id).first()
    if doctor:
        for key, value in doctor_data.model_dump().items():
            setattr(doctor, key, value)

        db.commit()
        db.refresh(doctor)

    return doctor


def delete_doctor(db: Session, doctor_id: int):
    doctor = db.query(Doctor).filter(Doctor.doctor_id == doctor_id).first()
    if doctor:
        db.delete(doctor)
        db.commit()

    return doctor