# Servicio de Orquestación

## Descripción

El Servicio de Orquestación actúa como coordinador entre los diferentes microservicios del sistema, gestionando flujos de trabajo complejos que requieren la interacción de múltiples componentes. Este servicio permite ejecutar procesos secuenciales y paralelos optimizando las operaciones del sistema.

## Características Principales

- Coordinación de flujos de trabajo entre servicios
- Gestión de procesos asíncronos
- Seguimiento de estados de ejecución
- Manejo de errores y reintentos
- Distribución de carga entre servicios

## Tecnologías

- **Framework**: FastAPI
- **Comunicación entre servicios**: HTTP/REST
- **Despliegue**: Docker

## API Endpoints

### `POST /process`

Inicia un proceso orquestado que puede involucrar múltiples servicios.

**Parámetros**:
- `process_type`: Tipo de proceso a ejecutar (obligatorio)
- `parameters`: Parámetros específicos para el proceso (obligatorio)

**Ejemplo de solicitud**:
```json
{
  "process_type": "document_analysis",
  "parameters": {
    "document_id": "doc123",
    "analysis_level": "full"
  }
}
```

**Respuesta exitosa**:
```json
{
  "process_id": "proc-789",
  "status": "started",
  "estimated_completion": "2025-04-15T15:30:00Z",
  "steps": [
    {"service": "ingestion", "status": "completed"},
    {"service": "analysis", "status": "pending"},
    {"service": "indexing", "status": "pending"}
  ]
}
```

## Estructura de Directorios

```
orchestration_service/
├── Dockerfile
├── requirements.txt
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── process.py
│   ├── models/
│   │   └── workflow.py
│   └── utils/
│       └── service_client.py
```

## Funcionamiento Interno

1. **Recepción de solicitud**: El servicio recibe una solicitud para iniciar un proceso.
2. **Definición del flujo**: Determina los pasos necesarios según el tipo de proceso.
3. **Ejecución coordinada**: Invoca a los servicios necesarios en el orden correcto.
4. **Supervisión**: Supervisa el progreso y maneja errores o fallos.
5. **Respuesta final**: Comunica el resultado cuando se completa el proceso.

## Desarrollo Local

Para ejecutar el servicio localmente:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8003
```

## Variables de Entorno

- `INGESTION_SERVICE_URL`: URL del servicio de ingesta
- `SEARCH_SERVICE_URL`: URL del servicio de búsqueda
- `LOG_LEVEL`: Nivel de logging (default: INFO)

## Dependencias

Todas las dependencias necesarias están listadas en el archivo `requirements.txt`.