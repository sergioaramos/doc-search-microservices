# Servicio de Ingesta

## Descripción

El Servicio de Ingesta es responsable de procesar los documentos PDF cargados al sistema. Este servicio extrae el texto de los PDFs utilizando técnicas avanzadas de Reconocimiento Óptico de Caracteres (OCR) con PaddleOCR, y luego indexa el contenido extraído en una base de datos Elasticsearch para facilitar la búsqueda.

## Características Principales

- Procesamiento de archivos PDF
- Extracción de texto con PaddleOCR
- Reconocimiento de texto multilenguaje
- Indexación en Elasticsearch
- Análisis por página y párrafo

## Tecnologías

- **Framework**: FastAPI
- **OCR**: PaddleOCR
- **Procesamiento de PDF**: PyMuPDF
- **Bases de datos**: Elasticsearch
- **Despliegue**: Docker

## API Endpoints

### `POST /ingestion/upload`

Permite subir un archivo PDF para procesamiento e indexación.

**Parámetros**:
- `file`: Archivo PDF (Form Data)

**Respuesta exitosa**:
```json
{
  "message": "Archivo procesado e indexado exitosamente.",
  "total_pages": 5
}
```

## Estructura de Directorios

```
ingestion_service/
├── Dockerfile
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes/
│   │   └── ingestion.py
│   └── utils/
│       ├── file_processor.py
│       └── elasticsearch_client.py
```

## Funcionamiento Interno

1. **Recepción de archivos**: El servicio recibe archivos PDF a través del endpoint `/ingestion/upload`.
2. **Procesamiento con OCR**: Utiliza PaddleOCR para extraer texto de cada página del documento.
3. **Extracción de metadatos**: Analiza y extrae información estructurada.
4. **Indexación**: Almacena el contenido extraído en Elasticsearch, indexándolo por página y párrafo.

## Desarrollo Local

Para ejecutar el servicio localmente:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

## Variables de Entorno

- `ELASTICSEARCH_URL`: URL del servidor Elasticsearch (por defecto: http://elasticsearch:9200)
- `ELASTICSEARCH_USER`: Usuario para Elasticsearch (opcional)
- `ELASTICSEARCH_PASSWORD`: Contraseña para Elasticsearch (opcional)

## Dependencias

Todas las dependencias necesarias están listadas en el archivo `requirements.txt`.