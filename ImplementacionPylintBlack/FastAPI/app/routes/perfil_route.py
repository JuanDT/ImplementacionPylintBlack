"""
Routes module for managing CRUD operations for the Perfil entity.

This module provides routes to create, read, update, and delete profiles.
"""

from fastapi import APIRouter
from models.perfil import Perfil
from services.perfil_service import PerfilService

perfil_router = APIRouter()
perfil_service = PerfilService()

@perfil_router.post("/perfil")
def create_perfil(perfil: Perfil):
    """
    Creates a new profile and adds it to the system.

    Args:
        perfil (Perfil): The profile data to create.

    Returns:
        Perfil: The created profile.
    """
    return perfil_service.create_perfil(perfil)

@perfil_router.get("/perfil")
def get_perfiles():
    """
    Retrieves all profiles in the system.

    Returns:
        List[Perfil]: A list of all profiles.
    """
    return perfil_service.get_all_perfiles()

@perfil_router.get("/perfil/{perfil_id}")
def get_perfil(perfil_id: int):
    """
    Retrieves a profile by its ID.

    Args:
        perfil_id (int): The ID of the profile to retrieve.

    Returns:
        Perfil: The profile with the given ID, or None if not found.
    """
    return perfil_service.get_perfil_by_id(perfil_id)

@perfil_router.put("/perfil/{perfil_id}")
def update_perfil(perfil_id: int, perfil: Perfil):
    """
    Updates an existing profile with new data.

    Args:
        perfil_id (int): The ID of the profile to update.
        perfil (Perfil): The updated profile data.

    Returns:
        Perfil: The updated profile.
    """
    return perfil_service.update_perfil(perfil_id, perfil)

@perfil_router.delete("/perfil/{perfil_id}")
def delete_perfil(perfil_id: int):
    """
    Deletes a profile from the system by its ID.

    Args:
        perfil_id (int): The ID of the profile to delete.

    Returns:
        None: The profile is deleted if found.
    """
    return perfil_service.delete_perfil(perfil_id)
