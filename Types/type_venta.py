from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import Venta as VentaModel

class Venta(MongoengineObjectType):

    class Meta:
        model = VentaModel
        interfaces = (Node,)