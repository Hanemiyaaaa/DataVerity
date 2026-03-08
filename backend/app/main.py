from fastapi import FastAPI
from app.database.session import engine
from sqlalchemy import text

app = FastAPI(
    title="DataVerity",
    version="0.1.0"
)

@app.get("/health", tags=["System"])
def health():
    return {
        "status": "ok"
    }

@app.get("/db-check")
def db_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": "connected", "result": result.scalar()}