import graphene
from graphene.relay import Node
from Type import Type

class Query(graphene.ObjectType):
    node = Node.Field()

Schema = graphene.Schema(query=Query, types=Type)