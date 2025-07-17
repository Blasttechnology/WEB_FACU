from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db.session_logic import BaseLogic as Base
import datetime

class Cliente(Base):
    __tablename__ = "cliente"

    id_cliente    = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre        = Column(String, nullable=False)
    apellido      = Column(String, nullable=False)
    email         = Column(String, unique=True, nullable=False)
    telefono      = Column(String, nullable=True)
    cuit          = Column(String, unique=True, nullable=False)
    direccion     = Column(String, nullable=True)
    activo        = Column(Boolean, default=True, nullable=False)
    fecha_alta    = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)