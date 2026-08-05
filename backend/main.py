from fastapi import FastAPI

from backend.database.db import engine, Base
from backend.models.patient import Patient

# Create database tables (if they don't already exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Healthcare Management & Analytics Platform",
    version="1.0"
)

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