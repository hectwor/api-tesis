from datetime import datetime
from Model import Producto as ProductoM
from Model import ProductoInput
from Type import Producto
import graphene
from graphene_mongo import MongoengineConnectionField


class ProductoAttribute:
    nombre = graphene.String(description="Nombre del producto.")
    categoria = graphene.ID(
        description="Categoria al que pertenece el producto.")
    codigo = graphene.String(description="Código del producto.")
    precio_venta = graphene.String(description="Precio de Venta del producto.")
    precio_compra = graphene.String(
        description="Precio que fue comprado del producto.")
    proveedor = graphene.ID(description="Proveedor del producto.")
    stock = graphene.String(description="Stock del producto.")
    descripcion = graphene.String(description="Descripción del producto.")
    estado = graphene.String(description="Estado del producto.")


class CreateProducto(graphene.Mutation):
    producto = graphene.Field(Producto)

    class Arguments:
        producto = ProductoInput()

    def mutate(self, info, producto):
        producto = ProductoM(producto)
        producto.save()
        return CreateProducto(producto=producto)

class UpdateProductoInput(graphene.InputObjectType, ProductoAttribute):
    """Arguments to update a producto."""
    id = graphene.ID(required=True, description="Global Id of the producto.")
