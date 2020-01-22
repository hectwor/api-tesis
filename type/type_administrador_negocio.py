from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from model.model_administrador_negocio import AdministradorNegocio as AdminisitradorNegocioModel

class AdministradorNegocio(MongoengineObjectType):

    class Meta:
        model = AdminisitradorNegocioModel
        interfaces = (Node,)