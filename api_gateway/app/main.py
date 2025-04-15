from fastapi import FastAPI
from app.routes import ingestion, search, orchestration
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
import logging

# Crear la aplicación FastAPI
app = FastAPI(title="API Gateway")

# Configuración básica de logs
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Habilitar CORS para el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar las rutas de cada microservicio
app.include_router(ingestion.router, prefix="/ingestion", tags=["Ingestion Service"])
app.include_router(search.router, prefix="/search", tags=["Search Service"])
app.include_router(orchestration.router, prefix="/orchestration", tags=["Orchestration Service"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API Gateway"}

# Manejador global para errores HTTP
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    logger.error(f"HTTP error in {request.method} {request.url}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "message": exc.detail,
            "status_code": exc.status_code,
        },
    )

# Manejador global para errores de validación
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.error(f"Validation error in {request.method} {request.url}: {exc}")
    return JSONResponse(
        status_code=422,
        content={
            "error": True,
            "message": "Error en la validación de la solicitud",
            "details": exc.errors(),
            "status_code": 422,
        },
    )

# Manejador global para cualquier otro error no capturado
@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unexpected error in {request.method} {request.url}: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "message": "Ocurrió un error interno en el API Gateway",
            "status_code": 500,
        },
    )