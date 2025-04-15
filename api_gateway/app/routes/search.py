from fastapi import APIRouter, HTTPException, Query
import httpx

router = APIRouter()

SEARCH_SERVICE_URL = "http://search_service:8002"

@router.get("/")
async def search_word(word: str = Query(..., description="Palabra clave para buscar")):
    """Redirige la búsqueda de palabras clave al servicio de búsqueda."""
    try:
        # Enviar la solicitud al servicio de búsqueda
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{SEARCH_SERVICE_URL}/search", params={"word": word})
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
