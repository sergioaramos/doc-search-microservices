# Servicio de Búsqueda

## Descripción

El Servicio de Búsqueda proporciona capacidades de búsqueda avanzada en los documentos indexados previamente por el Servicio de Ingesta. Permite buscar términos específicos dentro del contenido de los documentos PDF procesados, con resultados organizados por relevancia, documento y página.

## Características Principales

- Búsqueda de texto en documentos indexados
- Filtrado por relevancia
- Visualización contextual de resultados
- Búsqueda por documento o colección completa
- Integración con Elasticsearch para consultas eficientes

## Tecnologías

- **Framework**: FastAPI
- **Motor de búsqueda**: Elasticsearch
- **Despliegue**: Docker

## API Endpoints

### `GET /search`

Busca términos específicos en los documentos indexados.

**Parámetros**:
- `word`: Palabra o frase a buscar (obligatorio)
- `document_id`: ID del documento para limitar la búsqueda (opcional)
- `page_number`: Número de página específica para búsqueda (opcional)
- `limit`: Número máximo de resultados (por defecto: 10)

**Respuesta exitosa**:
```json
{
  "results": [
    {
      "document_name": "ejemplo.pdf",
      "page_number": 3,
      "text": "...contenido encontrado con la palabra buscada...",
      "confidence": 0.98,
      "score": 0.85
    }
  ],
  "total_hits": 1,
  "query_time_ms": 45
}
```

## Estructura de Directorios

```
search_service/
├── Dockerfile
├── requirements.txt
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── search.py
│   └── utils/
│       └── elasticsearch_client.py
```

## Funcionamiento Interno

1. **Recepción de consulta**: El servicio recibe una consulta de búsqueda con parámetros opcionales.
2. **Procesamiento de consulta**: Formatea y optimiza la consulta para Elasticsearch.
3. **Ejecución de búsqueda**: Realiza la búsqueda en el índice de Elasticsearch.
4. **Formateo de resultados**: Procesa y formatea los resultados de búsqueda para la presentación.

## Desarrollo Local

Para ejecutar el servicio localmente:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8002
```

## Variables de Entorno

- `ELASTICSEARCH_URL`: URL del servidor Elasticsearch (por defecto: http://elasticsearch:9200)
- `ELASTICSEARCH_USER`: Usuario para Elasticsearch (opcional)
- `ELASTICSEARCH_PASSWORD`: Contraseña para Elasticsearch (opcional)

## Dependencias

Todas las dependencias necesarias están listadas en el archivo `requirements.txt`.