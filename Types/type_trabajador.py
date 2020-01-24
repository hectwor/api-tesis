from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import Trabajador as TrabajadorModel

class Trabajador(MongoengineObjectType):

    class Meta:
        model = TrabajadorModel
        interfaces = (Node,)