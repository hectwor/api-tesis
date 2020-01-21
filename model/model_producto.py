from mongoengine import Document, EmbeddedDocument
from model.model_categoria_producto import CategoriaProducto
from model.model_proveedor import Proveedor
from mongoengine.fields import (
    ReferenceField, StringField, FloatField, IntField
)

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
