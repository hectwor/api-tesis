from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import Propuesta as PropuestaModel

class Propuesta(MongoengineObjectType):

    class Meta:
        model = PropuestaModel
        interfaces = (Node,)