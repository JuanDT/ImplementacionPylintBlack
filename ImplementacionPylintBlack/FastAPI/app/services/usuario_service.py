from peewee import DoesNotExist, IntegrityError
from fastapi import HTTPException
from models.usuario import Usuario
from database import UsuarioModel

class UsuarioService:
    def __init__(self):
        self.usuarios = []

    def create_usuario(self, usuario: Usuario):
        try:
            usuario_model = UsuarioModel.create(
                nombre=usuario.nombre,
                email=usuario.email,
                password=usuario.password
            )
            return usuario_model
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Usuario ya existe")

    def get_all_usuarios(self):
        return [usuario for usuario in UsuarioModel.select()]

    def get_usuario_by_id(self, usuario_id: int):
        try:
            return UsuarioModel.get(UsuarioModel.id == usuario_id)
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

    def update_usuario(self, usuario_id: int, usuario_data: Usuario):
        try:
            usuario = UsuarioModel.get(UsuarioModel.id == usuario_id)
            usuario.nombre = usuario_data.nombre
            usuario.email = usuario_data.email
            usuario.password = usuario_data.password
            usuario.save()
            return usuario
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

    def delete_usuario(self, usuario_id: int):
        try:
            usuario = UsuarioModel.get(UsuarioModel.id == usuario_id)
            usuario.delete_instance()
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
