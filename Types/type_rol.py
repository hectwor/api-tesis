from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import Rol as RolModel

class Rol(MongoengineObjectType):

    class Meta:
        model = RolModel
        interfaces = (Node,)