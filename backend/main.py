from fastapi import FastAPI

from backend.database.db import engine, Base
from backend.models.patient import Patient
from backend.models.doctor import Doctor

from backend.routes.patient_routes import router as patient_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Healthcare Platform")

app.include_router(patient_router)


@app.get("/")
def home():
    return {"message": "Smart Healthcare Platform API is Running Successfully"}