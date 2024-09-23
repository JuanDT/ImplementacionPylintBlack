"""
This module defines the Usuario model for the FastAPI application.

The Usuario model includes the fields:
- id: Unique identifier for the user
- name: Name of the user
- email: Email of the user
- password: Password of the user
"""

from pydantic import BaseModel

class Usuario(BaseModel):
    """
    Usuario model representing the details of a user.

    Attributes:
    - id: int, unique identifier for the user
    - name: str, the name of the user
    - email: str, the email of the user
    - password: str, the password of the user
    """
    id: int
    name: str
    email: str
    password: str
