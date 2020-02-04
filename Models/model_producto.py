from mongoengine import Document
from mongoengine.fields import (
    ReferenceField, StringField, FloatField, IntField
)
import graphene
from Model import (CategoriaProducto, Proveedor, CategoriaProductoInput, ProveedorInput)

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

class ProductoInput(graphene.InputObjectType):
    id = graphene.String()
    nombre = graphene.String()
    categoria = graphene.List(CategoriaProductoInput, required=False)
    codigo = graphene.String()
    precio_venta = graphene.Float()
    precio_compra = graphene.Float()
    proveedor = graphene.List(ProveedorInput, required=False)
    stock = graphene.Int()
    descripcion = graphene.String()
    estado = graphene.String()