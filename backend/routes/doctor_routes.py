from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.schemas.doctor_schema import DoctorCreate
from backend.controllers.doctor_controller import (
    fetch_doctors,
    add_doctor
)

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.get("/")
def get_doctors(db: Session = Depends(get_db)):
    return fetch_doctors(db)


@router.post("/")
def create_new_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db)
):
    return add_doctor(doctor, db)