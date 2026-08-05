from fastapi import FastAPI

from backend.database.db import engine, Base
from backend.models.patient import Patient
from backend.routes.patient_routes import router as patient_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Healthcare Management & Analytics Platform",
    version="1.0"
)

app.include_router(patient_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Healthcare Management & Analytics Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }