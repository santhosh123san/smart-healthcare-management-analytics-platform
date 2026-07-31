from fastapi import FastAPI

from backend.database.db import engine, Base
from backend.models.patient import Patient
from backend.models.doctor import Doctor

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Healthcare Platform")

@app.get("/")
def home():
    return {"message": "Smart Healthcare Platform API is Running Successfully"}