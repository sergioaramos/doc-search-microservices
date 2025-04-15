# Document Search Microservices

## Descripción General

Este proyecto implementa un sistema de búsqueda de documentos basado en una arquitectura de microservicios. Permite cargar archivos PDF, extraer texto utilizando técnicas de OCR (Reconocimiento Óptico de Caracteres) con PaddleOCR, indexar el contenido en Elasticsearch, y proporcionar un servicio de búsqueda para encontrar información dentro de los documentos.

## Arquitectura

El sistema está compuesto por los siguientes componentes:

1. **API Gateway**: Punto de entrada único para todas las solicitudes. Maneja el enrutamiento a los microservicios apropiados.

2. **Servicio de Ingesta**: Procesa documentos PDF subidos, extrae texto usando OCR, y almacena la información en Elasticsearch.

3. **Servicio de Búsqueda**: Proporciona capacidades de búsqueda en el contenido indexado.

4. **Servicio de Orquestación**: Coordina flujos de trabajo complejos entre servicios.

5. **Base de datos Elasticsearch**: Almacena y indexa el contenido extraído de los documentos para búsquedas eficientes.

6. **Frontend**: Interfaz de usuario para interactuar con el sistema (en desarrollo).

## Tecnologías Utilizadas

- **Backend**: Python, FastAPI, Uvicorn
- **OCR**: PaddleOCR, PyMuPDF
- **Base de datos**: Elasticsearch
- **Contenedorización**: Docker, Docker Compose

## Inicio Rápido

### Prerrequisitos

- Docker y Docker Compose
- Git

### Configuración

1. Clonar el repositorio:
```bash
git clone https://github.com/sergioaramos/doc-search-microservices.git
cd doc-search-microservices
```

2. Variables de entorno (crear archivo `.env` en la raíz):
```
ELASTICSEARCH_URL=http://elasticsearch:9200
ELASTICSEARCH_USER=elastic
ELASTICSEARCH_PASSWORD=changeme
```

3. Iniciar los servicios:
```bash
docker-compose up -d
```

4. Verificar que los servicios están funcionando:
```bash
curl http://localhost:8000/
```

## Endpoints API

### API Gateway (Puerto 8000)

- `GET /`: Verifica el estado del API Gateway
- `POST /ingestion/upload`: Carga un documento PDF para procesamiento
- `GET /search/?word=<término>`: Busca un término en los documentos indexados
- `POST /orchestration/process`: Inicia un proceso orquestado

## Estructura del Proyecto

```
docker-compose.yml
api_gateway/
    Dockerfile
    app/
        main.py
        routes/
            ingestion.py
            search.py
            orchestration.py
services/
    ingestion_service/
        Dockerfile
        app/
            main.py
            routes/
                ingestion.py
            utils/
                file_processor.py
                elasticsearch_client.py
    search_service/
        Dockerfile
        app/
            main.py
    orchestration_service/
        Dockerfile
        app/
            main.py
frontend/
    ...
```

## Desarrollo

Para desarrollar nuevos componentes o modificar los existentes, puede iniciar los servicios individualmente:

```bash
cd services/ingestion_service
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, asegúrese de seguir las convenciones de código del proyecto y añadir pruebas para nuevas funcionalidades.