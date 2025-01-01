# Establecer la imagen base
FROM python:3.10.12

WORKDIR /app/cafeteria_be

COPY requirements.txt .

# Instalar las dependencias de la aplicación
RUN pip install -r requirements.txt

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Establecer el comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]