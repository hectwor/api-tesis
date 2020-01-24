from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ReferenceField, StringField, IntField, FloatField
)
from Model import Compra, Producto

class DetalleCompra(Document):
    
    meta = {'collection': 'detalle_compra'}
    compra = ReferenceField(Compra)
    producto = ReferenceField(Producto)
    cantidad = IntField()
    precio = FloatField()
    descuento = FloatField()