from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField
)
import graphene

class Proveedor(Document):
    
    meta = {'collection': 'proveedor'}
    nombre = StringField()
    razon_social = StringField()
    telefono = StringField()
    correo = StringField()
    estado = StringField()

class ProveedorInput(graphene.InputObjectType):
    id = graphene.String()
    nombre = graphene.String()
    razon_social = graphene.String()
    telefono = graphene.String()
    correo = graphene.String()
    estado = graphene.String()