from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import Negocio as NegocioModel

class Negocio(MongoengineObjectType):

    class Meta:
        model = NegocioModel
        interfaces = (Node,)