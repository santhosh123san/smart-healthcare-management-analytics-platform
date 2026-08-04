from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.schemas.patient_schema import PatientCreate
from backend.controllers.patient_controller import (
    fetch_patients,
    add_patient
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    return fetch_patients(db)


@router.post("/")
def create_new_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    return add_patient(patient, db)


from backend.controllers.patient_controller import (
    modify_patient,
    remove_patient
)


@router.put("/{patient_id}")
def update_existing_patient(
    patient_id: int,
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    return modify_patient(patient_id, patient, db)


@router.delete("/{patient_id}")
def delete_existing_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    return remove_patient(patient_id, db)