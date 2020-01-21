from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField
)

class CategoriaProducto(Document):
    
    meta = {'collection': 'categoria_producto'}
    nombre = StringField()
    descripcion = StringField()
    estado = StringField()