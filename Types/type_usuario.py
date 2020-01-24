from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import Usuario as UsuarioModel

class Usuario(MongoengineObjectType):

    class Meta:
        model = UsuarioModel
        interfaces = (Node,)