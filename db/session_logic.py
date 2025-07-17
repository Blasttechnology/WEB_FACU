from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 2) URL de conexión a la base de datos de Lógica (Neon con SSL)
DATABASE_URL = "postgresql://Logica_owner:npg_7dQYbFSA6Teg@ep-lingering-fire-ac8gfzvf-pooler.sa-east-1.aws.neon.tech/Logica?sslmode=require&channel_binding=require"

# 3) Creamos el Engine y la sesión específica para Lógica
engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require", "channel_binding": "require"}
)
SessionLocalLogic = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 4) Base para los modelos de la capa de Lógica
BaseLogic = declarative_base()