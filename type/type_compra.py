from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from model.model_compra import Compra as CompraModel

class Compra(MongoengineObjectType):

    class Meta:
        model = CompraModel
        interfaces = (Node,)