from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Inicializar PaddleOCR

def process_pdf_with_ocr(file):
    """
    Procesa un archivo PDF para extraer texto, párrafos y ubicación.
    """
    import fitz  # PyMuPDF para manejo de PDFs

    pdf = fitz.open(stream=file.file.read(), filetype="pdf")
    total_pages = len(pdf)
    extracted_data = []

    for page_number in range(total_pages):
        page = pdf.load_page(page_number)
        pix = page.get_pixmap()  # Convertir página a imagen
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)  # Convertir imagen para OCR
        page_array = np.array(image)  # Convertir la imagen PIL a un numpy array

        # Usar PaddleOCR para extraer texto
        results = ocr.ocr(page_array, cls=True)
        page_text = []
        for line in results[0]:
            text = line[1][0]  # Obtener el texto
            confidence = line[1][1]  # Nivel de confianza
            page_text.append({"text": text, "confidence": confidence})

        extracted_data.append({
            "page": page_number + 1,
            "content": page_text
        })

    pdf.close()
    return {
        "total_pages": total_pages,
        "extracted_data": extracted_data
    }