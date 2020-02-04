from mongoengine import Document
from mongoengine.fields import (
    ReferenceField, StringField
)
from Model import Persona, Rol

class Usuario(Document):
    
    meta = {'collection': 'usuario'}
    rol = ReferenceField(Rol)
    persona = ReferenceField(Persona)
    estado = StringField()
    nombre = StringField()
    clave = StringField()