import os, sys

# --- esto sólo si estás ejecutando fuera del root, para que encuentre el paquete "models" ---
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db.session_logic import engine, BaseLogic

# IMPORTA AQUÍ TODOS TUS MODELOS DE LÓGICA PARA QUE SE REGISTREN
import models.Negocio.Cliente
# … cualquier otro modelo que hayas creado …

if __name__ == "__main__":
    print("📦 Creando todas las tablas de la capa Lógica…")
    BaseLogic.metadata.create_all(bind=engine)
    print("✅ Tablas creadas.")