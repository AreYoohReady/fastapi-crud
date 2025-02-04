from fastapi import FastAPI
from app.routers import tasks

app = FastAPI(
    title="To-Do List API",
    description="API para manejar una lista de tareas usando FastAPI",
    version="1.0.0"
)

# Incluir los routers
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de To-Do List"}
