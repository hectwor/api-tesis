from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField, ReferenceField, DateTimeField, FloatField
)
from model.model_proveedor import Proveedor
from model.model_usuario import Usuario

class Compra(Document):
    
    meta = {'collection': 'compra'}
    proveedor = ReferenceField(Proveedor)
    usuario = ReferenceField(Usuario)
    comprobante = StringField()
    fecha = DateTimeField()
    total = FloatField()
    estado = StringField()