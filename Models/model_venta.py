from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField,
    FloatField
)
from Model import Cliente, Usuario

class Venta(Document):
    
    meta = {'collection': 'venta'}
    cliente = ReferenceField(Cliente)
    usuario = ReferenceField(Usuario)
    comprobante = StringField()
    fecha = DateTimeField()
    total = FloatField()
    estado = StringField()