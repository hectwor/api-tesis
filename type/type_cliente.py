from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from model.model_cliente import Cliente as ClienteModel

class Cliente(MongoengineObjectType):

    class Meta:
        model = ClienteModel
        interfaces = (Node,)