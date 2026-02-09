@app.get("/version")
def version():
    return {"version": "0.0.2", "branch": "feature/version-endpoint"}

from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

@app.get("/")
def root():
    return {
        "ok": True,
        "message": "Версия 2. Привет.",
        "ts_utc": datetime.now(timezone.utc).isoformat()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
