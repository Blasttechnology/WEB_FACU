from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión a la base de datos Logic (Neon con SSL)
DATABASE_URL = 'postgresql://Logica_owner:npg_7dQYbFSA6Teg@ep-lingering-fire-ac8gfzvf-pooler.sa-east-1.aws.neon.tech/Logica?sslmode=require&channel_binding=require'

# Crear el motor
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocalLogic = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos de la lógica
BaseLogic = declarative_base()