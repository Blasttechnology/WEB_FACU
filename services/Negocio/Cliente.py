from sqlalchemy.orm import Session
from CRUD.Negocio.CRUD_Cliente import (
    crear_cliente, listar_clientes, obtener_cliente_por_id,
    actualizar_cliente, eliminar_cliente
)
from schemas.Negocio.Cliente import ClienteCreate, ClienteUpdate
from fastapi import HTTPException


def registrar_cliente(cliente_data: ClienteCreate, db: Session):
    return crear_cliente(db, cliente_data)


def listar_todos_los_clientes(db: Session):
    return listar_clientes(db)


def buscar_cliente(id_cliente: int, db: Session):
    cliente = obtener_cliente_por_id(db, id_cliente)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente


def editar_cliente(id_cliente: int, cliente_data: ClienteUpdate, db: Session):
    cliente_actualizado = actualizar_cliente(db, id_cliente, cliente_data)
    if not cliente_actualizado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente_actualizado


def borrar_cliente(id_cliente: int, db: Session):
    eliminado = eliminar_cliente(db, id_cliente)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return eliminado
