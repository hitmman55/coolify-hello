import os
from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "ok": True,
        "message": os.getenv("APP_MESSAGE", "Hello from Coolify"),
        "ts_utc": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": "0.0.2", "branch": "main"}
