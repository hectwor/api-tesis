import graphene
from graphene.relay import Node
from type.type_administrador_negocio import AdministradorNegocio
from type.type_categoria_producto import CategoriaProducto
from type.type_cliente import Cliente

class Query(graphene.ObjectType):
    node = Node.Field()

schema = graphene.Schema(query=Query, types=[
    AdministradorNegocio, 
    CategoriaProducto, 
    Cliente
    ])