"""
This module defines the Perfil model for the FastAPI application.

The Perfil model includes the fields:
- id: Unique identifier for the profile
- usuario_id: Foreign key referencing the Usuario model
- foto_perfil: Profile picture of the user
- biografia: Biography of the user
"""

from pydantic import BaseModel

class Perfil(BaseModel):
    """
    Perfil model representing the details of a user profile.

    Attributes:
    - id: int, unique identifier for the profile
    - usuario_id: int, foreign key linking to the user
    - foto_perfil: str, URL or path to the profile picture
    - biografia: str, biography of the user
    """
    id: int
    usuario_id: int  # Foreign Key
    foto_perfil: str
    biografia: str
