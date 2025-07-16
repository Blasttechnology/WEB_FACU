from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db.base import Base
import datetime

class Cliente(Base):
    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    cuit = Column(String(20), unique=True, nullable=False)
    direccion = Column(String(200), nullable=True)
    activo = Column(Boolean, default=True)
    fecha_alta = Column(DateTime, default=datetime.datetime.utcnow)