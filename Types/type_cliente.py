from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import Cliente as ClienteModel

class Cliente(MongoengineObjectType):

    class Meta:
        model = ClienteModel
        interfaces = (Node,)