"""
Routes module for managing CRUD operations for the Usuario entity.

This module provides routes to create, read, update, and delete users.
"""

from fastapi import APIRouter
from models.usuario import Usuario
from services.usuario_service import UsuarioService

usuario_router = APIRouter()
usuario_service = UsuarioService()

@usuario_router.post("/usuario")
def create_usuario(usuario: Usuario):
    """
    Creates a new user and adds it to the system.

    Args:
        usuario (Usuario): The user data to create.

    Returns:
        Usuario: The created user.
    """
    return usuario_service.create_usuario(usuario)

@usuario_router.get("/usuario")
def get_usuarios():
    """
    Retrieves all users in the system.

    Returns:
        List[Usuario]: A list of all users.
    """
    return usuario_service.get_all_usuarios()

@usuario_router.get("/usuario/{usuario_id}")
def get_usuario(usuario_id: int):
    """
    Retrieves a user by their ID.

    Args:
        usuario_id (int): The ID of the user to retrieve.

    Returns:
        Usuario: The user with the given ID, or None if not found.
    """
    return usuario_service.get_usuario_by_id(usuario_id)

@usuario_router.put("/usuario/{usuario_id}")
def update_usuario(usuario_id: int, usuario: Usuario):
    """
    Updates an existing user with new data.

    Args:
        usuario_id (int): The ID of the user to update.
        usuario (Usuario): The updated user data.

    Returns:
        Usuario: The updated user.
    """
    return usuario_service.update_usuario(usuario_id, usuario)

@usuario_router.delete("/usuario/{usuario_id}")
def delete_usuario(usuario_id: int):
    """
    Deletes a user from the system by their ID.

    Args:
        usuario_id (int): The ID of the user to delete.

    Returns:
        None: The user is deleted if found.
    """
    return usuario_service.delete_usuario(usuario_id)
