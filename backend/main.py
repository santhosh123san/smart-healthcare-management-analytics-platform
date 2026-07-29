from fastapi import FastAPI

app = FastAPI(
    title="Smart Healthcare Management & Analytics Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Smart Healthcare Management & Analytics Platform API is Running Successfully"
    }