from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import DetalleCompra as DetalleCompraModel

class DetalleCompra(MongoengineObjectType):

    class Meta:
        model = DetalleCompraModel
        interfaces = (Node,)