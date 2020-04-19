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

class ProductoGraph(graphene.ObjectType):
    nombre = graphene.String()
    categoria = graphene.Field(CategoriaProductoInput, required=False)
    codigo = graphene.String()
    precio_venta = graphene.Float()
    precio_compra = graphene.Float()
    proveedor = graphene.Field(ProveedorInput, required=False)
    stock = graphene.Int()
    descripcion = graphene.String()
    estado = graphene.String()

class ProductoInput(graphene.InputObjectType):
    nombre = graphene.String()
    categoria = graphene.InputField(CategoriaProductoInput, required=False)
    codigo = graphene.String()
    precio_venta = graphene.Float()
    precio_compra = graphene.Float()
    proveedor = graphene.InputField(ProveedorInput, required=False)
    stock = graphene.Int()
    descripcion = graphene.String()
    estado = graphene.String()