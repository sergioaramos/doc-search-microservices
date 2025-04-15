# Usar imagen oficial de Python
FROM python:3.10-slim

# Crear y establecer el directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]