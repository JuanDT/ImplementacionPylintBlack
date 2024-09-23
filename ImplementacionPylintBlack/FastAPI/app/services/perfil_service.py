from peewee import DoesNotExist, IntegrityError
from fastapi import HTTPException
from models.perfil import Perfil
from database import PerfilModel

class PerfilService:
    def __init__(self):
        self.perfiles = []

    def create_perfil(self, perfil: Perfil):
        try:
            perfil_model = PerfilModel.create(
                usuario_id=perfil.usuario_id,
                foto_perfil=perfil.foto_perfil,
                biografia=perfil.biografia
            )
            return perfil_model
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Perfil ya existe")

    def get_all_perfiles(self):
        return [perfil for perfil in PerfilModel.select()]

    def get_perfil_by_id(self, perfil_id: int):
        try:
            return PerfilModel.get(PerfilModel.id == perfil_id)
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")

    def update_perfil(self, perfil_id: int, perfil_data: Perfil):
        try:
            perfil = PerfilModel.get(PerfilModel.id == perfil_id)
            perfil.usuario_id = perfil_data.usuario_id
            perfil.foto_perfil = perfil_data.foto_perfil
            perfil.biografia = perfil_data.biografia
            perfil.save()
            return perfil
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")

    def delete_perfil(self, perfil_id: int):
        try:
            perfil = PerfilModel.get(PerfilModel.id == perfil_id)
            perfil.delete_instance()
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Perfil no encontrado")
