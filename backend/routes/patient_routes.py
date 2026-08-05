from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.db import SessionLocal
from backend.schemas.patient_schema import PatientCreate, PatientResponse
from backend.controllers.patient_controller import (
    get_patients_controller,
    get_patient_controller,
    create_patient_controller
)

router = APIRouter(prefix="/patients", tags=["Patients"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    return get_patients_controller(db)


@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    return get_patient_controller(patient_id, db)


@router.post("/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient_controller(patient, db)