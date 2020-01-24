from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import TipoPropuesta as TipoPropuestaModel

class TipoPropuesta(MongoengineObjectType):

    class Meta:
        model = TipoPropuestaModel
        interfaces = (Node,)