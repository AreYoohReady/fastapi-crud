# FastAPI CRUD - Gestión de Tareas 📝

## 📌 Descripción
Este proyecto es una API RESTful construida con **FastAPI** para la gestión de tareas. Implementa un CRUD básico y está contenerizado con **Docker**.

## 🚀 Características
- ✅ CRUD (Crear, Leer, Actualizar, Eliminar) de tareas 📋
- ✅ Base de datos SQLite con SQLAlchemy 🗄️
- ✅ Rutas organizadas con Routers de FastAPI 🔄
- ✅ Documentación automática con Swagger y ReDoc 📖
- ✅ Desplegado en Docker 🐳

## 📂 Estructura del Proyecto
Proyecto Crud Completo │── app │ ├── database │ ├── models │ ├── routers │ ├── schemas │ ├── main.py │── venv (Ignorado en .gitignore) │── Dockerfile │── docker-compose.yml │── requirements.txt │── README.md

## 🛠️ Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/AreYoohReady/fastapi-crud.git
cd fastapi-crud

2. crear entorno virtual e instalar depencdenciass

python -m venv venv
source venv/Scripts/activate  # En Windows
pip install -r requirements.txt

3. ejecutar el servidor fastapi

uvicorn app.main:app --reload
a API estará disponible en:

http://127.0.0.1:8000/docs (Swagger)
http://127.0.0.1:8000/redoc (ReDoc)

🐳 Docker

1. construir la imagen

docker build -t fastapi-crud .

2. ejecutar el contenedor

docker run -d -p 8000:8000 fastapi-crud

