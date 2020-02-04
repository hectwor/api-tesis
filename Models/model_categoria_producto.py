from mongoengine import Document, EmbeddedDocument
import graphene
from mongoengine.fields import (
    StringField
)

class CategoriaProducto(Document):
    
    meta = {'collection': 'categoria_producto'}
    nombre = StringField()
    descripcion = StringField()
    estado = StringField()

class CategoriaProductoInput(graphene.InputObjectType):
    id = graphene.String()
    nombre = graphene.String()
    categoria = graphene.String()
    codigo = graphene.String()