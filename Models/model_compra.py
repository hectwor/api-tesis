from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField, ReferenceField, DateTimeField, FloatField
)
from Model import Proveedor, Usuario

class Compra(Document):
    
    meta = {'collection': 'compra'}
    proveedor = ReferenceField(Proveedor)
    usuario = ReferenceField(Usuario)
    comprobante = StringField()
    fecha = DateTimeField()
    total = FloatField()
    estado = StringField()