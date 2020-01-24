from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField
)

class Proveedor(Document):
    
    meta = {'collection': 'proveedor'}
    nombre = StringField()
    razon_social = StringField()
    telefono = StringField()
    correo = StringField()
    estado = StringField()