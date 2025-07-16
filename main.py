# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from services.Cargo import Registrar_cargo, Listar_cargo, Actualizar_cargo, Eliminar_cargo
from services.Usuario import Registrar_usuario, Listar_usuario, Actualizar_usuario, Eliminar_usuario
from services.Permiso import Registrar_permiso, Listar_permiso, Actualizar_permiso, Eliminar_permiso
from schemas.Cargo import CargoCreate, CargoUpdate, Cargo as CargoResponse
from schemas.Usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse as UsuarioResponse
from schemas.Permiso import PermisoCreate, PermisoUpdate, Permiso as PermisoResponse
from schemas.Cargo_Permiso import CargoPermisoCreate, CargoPermisoResponse, CargoConPermisos, PermisoSimple
from services.Cargo_Permiso import (
    asignar_permiso_service,
    listar_permisos_por_cargo_service,
    eliminar_permiso_service,
    listar_cargos_con_permisos_service
)
from schemas.Negocio.Cliente import ClienteCreate, ClienteUpdate, ClienteResponse
from services.Negocio.Cliente import registrar_cliente, listar_todos_los_clientes, buscar_cliente, editar_cliente, borrar_cliente
from db.session import SessionLocal
from db.base import Base
import models


app = FastAPI()


# Dependencia para obtener la sesión de DB en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# --------------------------
#      RUTAS DE CARGO
# --------------------------

@app.post("/crearcargo", response_model=CargoResponse)
def create_cargo_endpoint(cargo_in: CargoCreate, db: Session = Depends(get_db)):
    try:
        cargo = Registrar_cargo(cargo_in, db)
        return cargo
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/listarcargo", response_model= list[CargoResponse])
def list_cargo_endpoint(db: Session = Depends(get_db)):
    return Listar_cargo(db)



@app.put("/actualizarcargo/{id_cargo}", response_model=CargoResponse)
def update_cargo_endpoint(id_cargo: int, cargo_in: CargoUpdate, db: Session = Depends(get_db)):
    try:
        return Actualizar_cargo(id_cargo, cargo_in, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
    
@app.delete("/deletecargo/{id_cargo}")
def delete_cargo_endpoint(id_cargo: int, db: Session = Depends(get_db)):
    try:
        return Eliminar_cargo(id_cargo, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# --------------------------
#      RUTAS DE USUARIO
# --------------------------

@app.post("/crearusuario", response_model=UsuarioResponse)
def create_usuario_endpoint(datos_usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        usuario = Registrar_usuario(datos_usuario, db)
        return usuario
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e.detail))
    except Exception as a:
        raise HTTPException(status_code=500, detail=str(a))

@app.get("/listarusuario", response_model= list[UsuarioResponse])
def list_usuario_endpoint(db: Session = Depends(get_db)):
    return Listar_usuario(db)



@app.put("/actualizarusuario/{id_usuario}", response_model=UsuarioResponse)
def update_usuario_endpoint(id_usuario: int, datos_usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    try:
        return Actualizar_usuario(id_usuario, datos_usuario, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
    
@app.delete("/deleteusuario/{id_usuario}")
def delete_usuario_endpoint(id_usuario: int, db: Session = Depends(get_db)):
    try:
        return Eliminar_usuario(id_usuario, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# --------------------------
#      RUTAS DE PERMISOS
# --------------------------

@app.post("/crearpermiso", response_model=PermisoResponse)
def create_permiso_endpoint(permiso_in: PermisoCreate, db: Session = Depends(get_db)):
    try:
        permiso = Registrar_permiso(permiso_in, db)
        return permiso
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/listarpermiso", response_model= list[PermisoResponse])
def list_permiso_endpoint(db: Session = Depends(get_db)):
    return Listar_permiso(db)



@app.put("/actualizarpermiso/{id_permiso}", response_model=PermisoResponse)
def update_permiso_endpoint(id_permiso: int, permiso_in: PermisoUpdate, db: Session = Depends(get_db)):
    try:
        return Actualizar_permiso(id_permiso, permiso_in, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
    
@app.delete("/deletepermiso/{id_permiso}")
def delete_permiso_endpoint(id_permiso: int, db: Session = Depends(get_db)):
    try:
        return Eliminar_permiso(id_permiso, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ------------------------------
#      RUTAS DE CARGO_PERMISO
# ------------------------------

@app.post("/asignar_permiso", response_model=CargoPermisoResponse)
def asignar_permiso(datos: CargoPermisoCreate, db: Session = Depends(get_db)):
    return asignar_permiso_service(db, datos.id_cargo, datos.id_permiso)


# Obtener solo los permisos de un cargo por ID (con nombre y descripción)
@app.get("/permisos_por_cargo/{id_cargo}", response_model=List[PermisoSimple])
def permisos_por_cargo(id_cargo: int, db: Session = Depends(get_db)):
    permisos = listar_permisos_por_cargo_service(id_cargo, db)
    if not permisos:
        raise HTTPException(status_code=404, detail="El cargo no tiene permisos asignados o no existe.")
    return permisos

@app.delete("/eliminar_permiso_cargo")
def eliminar_permiso(id_cargo: int, id_permiso: int, db: Session = Depends(get_db)):
    return eliminar_permiso_service(db, id_cargo, id_permiso)

@app.get("/cargos_con_permisos", response_model=list[CargoConPermisos])
def listar_cargos_con_permisos(db: Session = Depends(get_db)):
    return listar_cargos_con_permisos_service(db)

# ------------------------------
#      RUTAS DE CLIENTE
# ------------------------------

@app.post("/clientes", response_model=ClienteResponse)
def crear_cliente_endpoint(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return registrar_cliente(cliente, db)

@app.get("/clientes", response_model=list[ClienteResponse])
def listar_clientes_endpoint(db: Session = Depends(get_db)):
    return listar_todos_los_clientes(db)

@app.get("/clientes/{id_cliente}", response_model=ClienteResponse)
def obtener_cliente_endpoint(id_cliente: int, db: Session = Depends(get_db)):
    return buscar_cliente(id_cliente, db)

@app.put("/clientes/{id_cliente}", response_model=ClienteResponse)
def actualizar_cliente_endpoint(id_cliente: int, cliente: ClienteUpdate, db: Session = Depends(get_db)):
    return editar_cliente(id_cliente, cliente, db)

@app.delete("/clientes/{id_cliente}")
def eliminar_cliente_endpoint(id_cliente: int, db: Session = Depends(get_db)):
    return borrar_cliente(id_cliente, db)


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)