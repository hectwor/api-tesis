from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import CategoriaProducto as CategoriaProductoModel

class CategoriaProducto(MongoengineObjectType):

    class Meta:
        model = CategoriaProductoModel
        interfaces = (Node,)