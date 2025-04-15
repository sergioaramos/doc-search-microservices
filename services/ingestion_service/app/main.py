from fastapi import FastAPI
from app.routes import ingestion

# Crear la aplicación FastAPI
app = FastAPI(title="Ingestion Service")

# Registrar las rutas del servicio de ingesta
app.include_router(ingestion.router, prefix="/ingestion", tags=["Ingestion Service"])

@app.get("/")
async def root():
    return {"message": "Ingestion Service is up and running!"}