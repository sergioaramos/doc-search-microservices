# API Gateway

## Descripción

El API Gateway actúa como punto de entrada único para todas las solicitudes del sistema de búsqueda de documentos. Es responsable de enrutar las peticiones a los microservicios correspondientes, proporcionando una interfaz unificada para los clientes.

## Características Principales

- Punto de entrada único para todos los microservicios
- Enrutamiento de solicitudes
- Manejo centralizado de errores
- Middleware CORS para comunicación con el frontend
- Validación de solicitudes

## Tecnologías

- **Framework**: FastAPI
- **Cliente HTTP**: HTTPX para comunicación asíncrona con microservicios
- **Despliegue**: Docker

## API Endpoints

### Endpoints de Ingesta
- `POST /ingestion/upload`: Enruta solicitudes para cargar documentos PDF al servicio de ingesta.

### Endpoints de Búsqueda
- `GET /search/?word=<término>`: Enruta solicitudes de búsqueda al servicio de búsqueda.

### Endpoints de Orquestación
- `POST /orchestration/process`: Enruta solicitudes de procesamiento al servicio de orquestación.

### Endpoint de Salud
- `GET /`: Verifica que el API Gateway esté funcionando correctamente.

## Estructura de Directorios

```
api_gateway/
├── Dockerfile
├── requirements.txt
├── app/
│   ├── main.py
│   └── routes/
│       ├── ingestion.py
│       ├── search.py
│       └── orchestration.py
```

## Funcionamiento Interno

1. **Recepción de solicitudes**: El gateway recibe todas las solicitudes entrantes.
2. **Validación y procesamiento**: Valida las solicitudes y aplica middlewares necesarios.
3. **Enrutamiento**: Dirige las solicitudes al microservicio apropiado.
4. **Manejo de respuestas**: Procesa las respuestas y maneja errores de forma centralizada.

## Desarrollo Local

Para ejecutar el gateway localmente:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## Documentación de la API

La documentación interactiva generada automáticamente por FastAPI está disponible en:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Variables de Entorno

- `INGESTION_SERVICE_URL`: URL del servicio de ingesta (por defecto: http://ingestion_service:8001)
- `SEARCH_SERVICE_URL`: URL del servicio de búsqueda (por defecto: http://search_service:8002)
- `ORCHESTRATION_SERVICE_URL`: URL del servicio de orquestación (por defecto: http://orchestration_service:8003)
- `LOG_LEVEL`: Nivel de logging (default: INFO)