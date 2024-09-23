"""
Database models for the FastAPI application.

This module contains the database models used for the application,
including UsuarioModel and PerfilModel.
"""

from datetime import date
import os
from dotenv import load_dotenv
from peewee import *

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos MySQL
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

class BaseModel(Model):  # pylint: disable=too-few-public-methods
    """
    Base model that sets up the database for all tables.

    This class ensures all models inherit the database connection.
    """
    class Meta:
        database = database

class UsuarioModel(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Model representing a user.

    Attributes:
        id (int): Primary key for the user.
        nombre (str): Name of the user.
        email (str): Email of the user (must be unique).
        password (str): Password for the user.
    """
    
    id = AutoField(primary_key=True)
    nombre = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    password = CharField(max_length=255)

    class Meta:
        table_name = "usuarios"

class PerfilModel(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Model representing a user's profile.

    Attributes:
        id (int): Primary key for the profile.
        usuario_id (int): Foreign key referencing the user.
        foto_perfil (str): URL or path to the user's profile picture.
        biografia (str): Biography or description of the user.
    """
    
    id = AutoField(primary_key=True)
    usuario_id = ForeignKeyField(UsuarioModel, backref="perfiles", on_delete="CASCADE")
    foto_perfil = CharField(max_length=255, null=True)
    biografia = TextField(null=True)

    class Meta:
        table_name = "perfiles"

# Conectar a la base de datos y crear las tablas si no existen
def initialize_database():
    """
    Connect to the database and create tables if they do not exist.

    This function initializes the connection to the database and ensures that
    the tables for UsuarioModel and PerfilModel are created.
    """
    with database:
        database.create_tables([UsuarioModel, PerfilModel])
