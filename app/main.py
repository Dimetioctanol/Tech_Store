from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.v1.endpoints.auth import router as auth_router


app = FastAPI(
    title="TechStore API",
    version="1.0.0",
    description="E-commerce de artículos tecnológicos"
)

app.include_router(auth_router, prefix= "/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "TechStore API corriendo"}