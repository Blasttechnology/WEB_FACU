from db.base    import Base
from db.session_logic import engine

print("Creando todas las tablas...")
Base.metadata.create_all(bind=engine)
