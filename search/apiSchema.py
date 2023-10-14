import graphene
from graphene_django import DjangoObjectType

from search.models import *
from search.views import *


class Query(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)