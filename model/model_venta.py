from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField,
    FloatField
)
from model.model_cliente import Cliente
from model.model_usuario import Usuario

class Venta(Document):
    
    meta = {'collection': 'venta'}
    cliente = ReferenceField(Cliente)
    usuario = ReferenceField(Usuario)
    comprobante = StringField()
    fecha = DateTimeField()
    total = FloatField()
    estado = StringField()