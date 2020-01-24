from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import DetalleVenta as DetalleVentaModel

class DetalleVenta(MongoengineObjectType):

    class Meta:
        model = DetalleVentaModel
        interfaces = (Node,)