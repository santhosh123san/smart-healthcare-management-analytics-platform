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



from backend.services.doctor_service import (
    update_doctor,
    delete_doctor
)


def modify_doctor(doctor_id: int, doctor_data: DoctorCreate, db: Session):
    return update_doctor(db, doctor_id, doctor_data)


def remove_doctor(doctor_id: int, db: Session):
    return delete_doctor(db, doctor_id)