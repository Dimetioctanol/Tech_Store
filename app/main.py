from fastapi import FastAPI
from app.db.database import engine, Base

app = FastAPI(
    title="TechStore API",
    version="1.0.0",
    description="E-commerce de articulos tecnológicos"
)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "TechStore API corriendo"}