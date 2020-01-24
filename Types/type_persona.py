from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import Persona as PersonaModel

class Persona(MongoengineObjectType):

    class Meta:
        model = PersonaModel
        interfaces = (Node,)