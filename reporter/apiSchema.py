import graphene
import datetime
from graphene_django import DjangoObjectType

from reporter.models import Reporter

class ReporterType(DjangoObjectType):
    class Meta:
        model = Reporter
        fields = "__all__"

class Query(graphene.ObjectType):
    reporters = graphene.List(ReporterType, first = graphene.Int(), skip = graphene.Int())
    reporter = graphene.Field(ReporterType, id=graphene.Int())

    def resolve_reporters(self, info, first=None, skip=None, **kwargs):
        reporters = Reporter.objects.all()
        if skip:
            reporters = reporters[skip:]
        if first:
            reporters = reporters[:first]

        return reporters
    
    def resolve_reporter(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = Reporter.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None

schema = graphene.Schema(query=Query)

# Test Query

# Reporter Query
# query {
#   reporters {
#     id
#     name
#     email
#     phone
#     address
#     created_at
#     updated_at
#     total_view
#   }
# }
#

# Reporters Query with pagination
# query {
#   reporters(first: 2, skip: 1) {
#     id
#     name
#     email
#     phone
#     address
#     created_at
#     updated_at
#     total_view
#   }
# }
#

