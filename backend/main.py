from fastapi import FastAPI

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


@app.get("/")
def home():
    return {"message": "Smart Healthcare Platform API is Running Successfully"}