from fastapi import FastAPI
from .api import analyze

app = FastAPI(title="LLM Stream Analyzer")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(analyze.router, prefix="/api")
