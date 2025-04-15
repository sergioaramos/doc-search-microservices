from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv("../../.env")

# Obtener las variables de entorno
es_host = os.getenv("ELASTICSEARCH_URL")
es_user = os.getenv("ELASTICSEARCH_USER")
es_password = os.getenv("ELASTICSEARCH_PASSWORD")
es_hosts = [es_host]

# Conectar a Elasticsearch
es = Elasticsearch(
    hosts=es_hosts,
    verify_certs=False  # Solo para pruebas, omite la verificación del certificado SSL
)

def index_pdf_data(file_name, data):
    """
    Indexa los datos extraídos de un PDF en Elasticsearch.
    """
    print(f"Simulando indexación del archivo: {file_name}")
    print(f"Datos procesados: {data}")
    for page in data["extracted_data"]:
        page_number = page["page"]
        for paragraph in page["content"]:
            doc = {
                "file_name": file_name,
                "page_number": page_number,
                "text": paragraph["text"],
                "confidence": paragraph["confidence"],
                "total_pages": data["total_pages"]
            }
            res = es.index(index="pdf_documents", document=doc)