from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

ORCHESTRATION_SERVICE_URL = "http://orchestration_service:8003"

@router.post("/process")
async def orchestrate_process(data: dict):
    """Coordina procesos complejos a través del servicio de orquestación."""
    try:
        # Enviar la solicitud al servicio de orquestación
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{ORCHESTRATION_SERVICE_URL}/process", json=data)
            response.raise_for_status() # Lanza un error si el código HTTP es >= 400
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