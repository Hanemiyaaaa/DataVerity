from fastapi import FastAPI

app = FastAPI(
    title="DataVerity",
    version="0.1.0"
)

@app.get("/health", tags=["System"])
def health():
    return {
        "status": "ok"
    }