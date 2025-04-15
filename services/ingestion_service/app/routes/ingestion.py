from fastapi import APIRouter, UploadFile, HTTPException, File
from app.utils.file_processor import process_pdf_with_ocr
from app.utils.elasticsearch_client import index_pdf_data

router = APIRouter()

@router.post("/upload")
async def upload_and_process_pdf(file: UploadFile = File(...)):
    """
    Recibe un archivo PDF, extrae texto usando PaddleOCR, y lo indexa en Elasticsearch.
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400, detail="El archivo subido no es un PDF válido."
        )

    try:
        # Procesar el archivo con PaddleOCR
        processed_data = process_pdf_with_ocr(file)

        # Indexar los datos en Elasticsearch
        index_pdf_data(file.filename, processed_data)

        return {
            "message": "Archivo procesado e indexado exitosamente.",
            "total_pages": processed_data["total_pages"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ocurrió un error al procesar el archivo: {str(e)}"
        )