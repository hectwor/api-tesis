from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from model.model_categoria_producto import CategoriaProducto as CategoriaProductoModel

class CategoriaProducto(MongoengineObjectType):

    class Meta:
        model = CategoriaProductoModel
        interfaces = (Node,)