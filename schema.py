import graphene
from datetime import datetime
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Type import Type, Cliente, Persona, Usuario, Producto
from Model import Cliente as ClienteM
from Model import Producto as ProductoM
from Schemas.schema_producto import CreateProducto

class Query(graphene.ObjectType):
    productos = graphene.List(Producto)
    
    def resolve_productos(self, info):
    	return list(ProductoM.objects.all())

class Mutation(graphene.ObjectType):
    crearProducto = CreateProducto.Field()

Schema = graphene.Schema(query=Query,mutation=Mutation, types=Type)
