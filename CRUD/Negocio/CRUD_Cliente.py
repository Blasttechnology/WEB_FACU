from sqlalchemy.orm import Session
from models.Negocio.Cliente import Cliente
from schemas.Negocio.Cliente import ClienteCreate, ClienteUpdate


def crear_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = Cliente(**cliente.model_dump())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def listar_clientes(db: Session):
    return db.query(Cliente).all()


def obtener_cliente_por_id(db: Session, id_cliente: int):
    return db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()


def actualizar_cliente(db: Session, id_cliente: int, cliente_update: ClienteUpdate):
    db_cliente = obtener_cliente_por_id(db, id_cliente)
    if not db_cliente:
        return None
    for field, value in cliente_update.model_dump(exclude_unset=True).items():
        setattr(db_cliente, field, value)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def eliminar_cliente(db: Session, id_cliente: int):
    db_cliente = obtener_cliente_por_id(db, id_cliente)
    if not db_cliente:
        return None
    db.delete(db_cliente)
    db.commit()
    return db_cliente