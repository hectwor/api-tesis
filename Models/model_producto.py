from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    ReferenceField, StringField, FloatField, IntField
)
from Model import CategoriaProducto, Proveedor

class Producto(Document):
    
    meta = {'collection': 'producto'}
    nombre = StringField()
    categoria = ReferenceField(CategoriaProducto)
    codigo = StringField()
    precio_venta = FloatField()
    precio_compra = FloatField()
    proveedor = ReferenceField(Proveedor)
    stock = IntField()
    descripcion = StringField()
    estado = StringField()
