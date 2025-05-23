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
    reporter = graphene.Field(ReporterType, uId=graphene.String())

    def resolve_reporters(self, info, first=None, skip=None, **kwargs):
        reporters = Reporter.objects.all()
        if skip:
            reporters = reporters[skip:]
        if first:
            reporters = reporters[:first]

        return reporters
    
    def resolve_reporter(self, info, uId, **kwargs):
        id = kwargs.get('id')
        if uId is not None:
            obj = Reporter.objects.get(uniqueId=uId)
            return obj
        # elif id is not None:
        #     obj = Reporter.objects.get(pk=id)
        #     obj.total_view = obj.total_view + 1
        #     obj.save()
        #     return obj
        else:
            return None
    
class Mutation(graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
