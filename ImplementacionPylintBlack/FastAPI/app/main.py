"""
Módulo principal para la configuración de la aplicación FastAPI.

Este módulo configura la aplicación FastAPI, gestiona el ciclo de vida de la conexión
a la base de datos e incluye las rutas.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from helpers.api_key_auth import get_api_key
from starlette.responses import RedirectResponse
from database import database as connection
from routes.usuario_route import usuario_router
from routes.perfil_route import perfil_router

@asynccontextmanager
async def manage_lifespan(_app: FastAPI):
    """
    Gestiona la duración de la aplicación FastAPI.

    Asegura que la conexión a la base de datos se abra y cierre correctamente.
    """
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(
    title="Microservicio de Usuarios y Perfiles",
    version="1.0",
    contact={
        "name": "Juan David Toro Mesa",
        "url": "https://github.com/JuanDT",
        "email": "juandavidtoromesa2@gmail.com",
    },
    lifespan=manage_lifespan
)

@app.get("/")
async def read_root():
    """
    Redirige la ruta raíz a la documentación de la API.

    Devuelve una respuesta de redirección a la página de documentación.
    """
    return RedirectResponse(url="/docs")

app.include_router(usuario_router,
                   prefix="/usuarios",
                   tags=["Usuarios"],
                   dependencies=[Depends(get_api_key)])

app.include_router(perfil_router,
                   prefix="/perfiles",
                   tags=["Perfiles"],
                   dependencies=[Depends(get_api_key)])
