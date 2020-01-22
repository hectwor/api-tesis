from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ReferenceField, StringField
)
from model.model_persona import Persona
from model.model_rol import Rol

class Usuario(Document):
    
    meta = {'collection': 'usuario'}
    rol = ReferenceField(Rol)
    persona = ReferenceField(Persona)
    estado = StringField()
    nombre = StringField()
    clave = StringField()