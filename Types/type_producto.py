from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import Producto as ProductoModel

class Producto(MongoengineObjectType):

    class Meta:
        model = ProductoModel