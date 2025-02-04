from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import enum

# Definir estados posibles de la tarea
class TaskStatus(str, enum.Enum):
    pendiente = "pendiente"
    en_progreso = "en_progreso"
    completada = "completada"

# Esquema de entrada para crear una tarea
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pendiente

# Esquema de salida para mostrar una tarea
class TaskResponse(TaskCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
