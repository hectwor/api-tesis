from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ReferenceField, StringField
)
from Model import Usuario

class AdministradorNegocio(Document):
    
    meta = {'collection': 'administrador_negocio'}
    usuario = ReferenceField(Usuario)
    estado = StringField()
    token = StringField()