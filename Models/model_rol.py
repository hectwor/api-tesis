from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField
)

class Rol(Document):
    
    meta = {'collection': 'rol'}
    nombre = StringField()
    descripcion = StringField()
    estado = StringField()