from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import TipoNegocio as TipoNegocioModel

class TipoNegocio(MongoengineObjectType):

    class Meta:
        model = TipoNegocioModel
        interfaces = (Node,)