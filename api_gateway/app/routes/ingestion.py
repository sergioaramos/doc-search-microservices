import httpx
from fastapi import APIRouter, HTTPException, UploadFile

router = APIRouter()

INGESTION_SERVICE_URL = "http://ingestion_service:8001"

@router.post("/upload")
async def upload_pdf(file: UploadFile):
    """Envía un archivo PDF al servicio de ingesta."""
    try:
        # Enviar el archivo al servicio de ingesta
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{INGESTION_SERVICE_URL}/upload", 
                files={"file": file.file}
            )
            response.raise_for_status()  # Lanza un error si el código HTTP es >= 400
        return response.json()

    except httpx.RequestError as e:
        # Error de conexión o tiempo de espera
        raise HTTPException(
            status_code=503,
            detail=f"Error al conectarse con el servicio de ingesta: {str(e)}"
        )

    except httpx.HTTPStatusError as e:
        # Respuesta HTTP con error (404, 500, etc.)
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Error en el servicio de ingesta: {e.response.text}"
        )
