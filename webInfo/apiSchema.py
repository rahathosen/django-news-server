import graphene
from graphene_django import DjangoObjectType

from webInfo.models import *
from news.models import *
from categories.models import *
from article.models import *
from feature.models import *

class WebsiteInfoType(DjangoObjectType):
    class Meta:
        model = WebsiteInfo
        fields = "__all__"

class NavigationType(DjangoObjectType):
    class Meta:
        model = Navigation
        fields = "__all__"

class PollType(DjangoObjectType):
    class Meta:
        model = Poll
        fields = "__all__"

class HeadLineType(DjangoObjectType):
    class Meta:
        model = HeadLine
        fields = "__all__"

class BreakingNewsType(DjangoObjectType):
    class Meta:
        model = BreakingNews
        fields = "__all__"

class CoverType(DjangoObjectType):
    class Meta:
        model = Cover
        fields = "__all__"    

class UpdatePoll(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        question = graphene.String()
        option_one = graphene.String()
        option_two = graphene.String()
        option_three = graphene.String()
        option_one_count = graphene.Int()
        option_two_count = graphene.Int()
        option_three_count = graphene.Int()
        created_at = graphene.DateTime()
        end_at = graphene.DateTime()

    poll = graphene.Field(PollType)

    @classmethod
    def mutate(cls, root, info, id, question, option_one, option_two, option_three, option_one_count, option_two_count, option_three_count, created_at, end_at, total_view):
        poll = Poll.objects.get(pk=id)
        poll.question = question
        poll.option_one = option_one
        poll.option_two = option_two
        poll.option_three = option_three
        poll.option_one_count = option_one_count
        poll.option_two_count = option_two_count
        poll.option_three_count = option_three_count
        poll.created_at = created_at
        poll.end_at = end_at
    
        poll.save()
        return UpdatePoll(poll=poll)


class Query(graphene.ObjectType):
    websiteInfo = graphene.Field(WebsiteInfoType)
    navigation = graphene.Field(NavigationType)
    headLines = graphene.Field(HeadLineType)
    breakingNews = graphene.Field(BreakingNewsType)
    cover = graphene.Field(CoverType)
    
    poll = graphene.Field(PollType, id=graphene.Int())
    all_poll = graphene.List(PollType)

    
    def resolve_websiteInfo(self, info, **kwargs):
        obj = WebsiteInfo.objects.last()
        return obj
    
    def resolve_headLines(self, info, **kwargs):
        obj = HeadLine.objects.last()
        return obj

    def resolve_navigation(self, info, **kwargs):
        return Navigation.objects.last()
    
    def resolve_breakingNews(self, info, **kwargs):
        oj = BreakingNews.objects.last()
        return oj
    
    def resolve_cover(self, info, **kwargs):
        return Cover.objects.last()

    def resolve_poll(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = Poll.objects.get(pk=id)
            return obj
        else:
            return None
        
    def resolve_all_poll(self, info, **kwargs):

        allP =  Poll.objects.all()
        return allP
    
class Mutation(graphene.ObjectType):
    update_poll = UpdatePoll.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
