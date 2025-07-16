from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: Optional[str] = None
    cuit: str
    direccion: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    cuit: Optional[str] = None
    direccion: Optional[str] = None
    activo: Optional[bool] = None

class ClienteResponse(ClienteBase):
    id_cliente: int
    activo: bool
    fecha_alta: datetime

    class Config:
        from_attributes = True