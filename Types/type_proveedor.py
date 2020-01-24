from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from Model import Proveedor as ProveedorModel

class Proveedor(MongoengineObjectType):

    class Meta:
        model = ProveedorModel
        interfaces = (Node,)