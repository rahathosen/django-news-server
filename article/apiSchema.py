import datetime
import graphene
from graphene_django import DjangoObjectType

from article.models import Article, ArticleCategory, ArticleWritter

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = "__all__"

class ArticleCategoryType(DjangoObjectType):
    class Meta:
        model = ArticleCategory
        fields = "__all__"

class ArticleWritterType(DjangoObjectType):
    class Meta:
        model = ArticleWritter
        fields = "__all__"

class Query(graphene.ObjectType):
    articles_posts = graphene.List(ArticleType, first = graphene.Int(), skip = graphene.Int())
    article_post = graphene.Field(ArticleType, uId=graphene.String())
    article_categories = graphene.List(ArticleCategoryType, first = graphene.Int(), skip = graphene.Int())
    article_category = graphene.Field(ArticleCategoryType, categoryuId=graphene.String())
    article_writters = graphene.List(ArticleWritterType, first = graphene.Int(), skip = graphene.Int())
    article_writter = graphene.Field(ArticleWritterType, writteruId=graphene.String())

    article_by_category = graphene.List(ArticleType, categoryuId=graphene.String())
    article_by_writter = graphene.List(ArticleType, writteruId=graphene.String())

    today_articles = graphene.List(ArticleType)
    last_week_popular_article  = graphene.List(ArticleType)
    last_month_popular_article = graphene.List(ArticleType)

    popular_article_by_category_last_month = graphene.List(ArticleType, category_uId=graphene.String())
    popular_article_by_writter = graphene.List(ArticleType, writter_uId=graphene.String())

    related_article_by_category_last_month = graphene.List(ArticleType, category_uId=graphene.String())
    related_article_by_writter_last_ten = graphene.List(ArticleType, writter_uId=graphene.String())


    def resolve_articles_posts(self, info, first=None, skip=None, **kwargs):
        articles = Article.objects.all().filter(status=1, editor_reviewed=1)
        if skip:
            articles = articles[skip:]
        if first:
            articles = articles[:first]

        return articles
    
    def resolve_article_post(self, info, uId, **kwargs):

        if uId is not None:
            obj = Article.objects.get(uniqueId=uId, status=1, editor_reviewed=1)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        else:
            return None
    
    def resolve_article_categories(self, info, first=None, skip=None, **kwargs):
        article_categories = ArticleCategory.objects.all().filter(status=1)
        if skip:
            article_categories = article_categories[skip:]
        if first:
            article_categories = article_categories[:first]

        return article_categories
    
    def resolve_article_category(self, info, categoryuId, **kwargs):
        if categoryuId is not None:
            obj = ArticleCategory.objects.get(uniqueId=categoryuId, status = 1)
            return obj
        return None
    
    def resolve_article_writters(self, info, first=None, skip=None, **kwargs):
        article_writters = ArticleWritter.objects.all()
        if skip:
            article_writters = article_writters[skip:]
        if first:
            article_writters = article_writters[:first]

        return article_writters
    
    def resolve_article_writter(self, writteruId, info, **kwargs):
        if writteruId is not None:
            obj = ArticleWritter.objects.get(uniqueId=writteruId)
            return obj
        return None

    def resolve_article_by_category(self, info, categoryuId, **kwargs):
        if categoryuId is not None:
            obj = Article.objects.filter(category__uniqueId=categoryuId, status=1, editor_reviewed=1)

            return obj
        return None
    
    def resolve_article_by_writter(self, info, writteruId, **kwargs):
        if writteruId is not None:
            obj = Article.objects.filter(writter__uniqueId=writteruId, status=1, editor_reviewed=1)
            return obj
        return None
    
    def resolve_today_articles(self, info, **kwargs):
        return Article.objects.filter(created_at__date=datetime.date.today(),status=1, editor_reviewed=1)
    
    def resolve_last_week_popular_article(self, info, **kwargs):
        return Article.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=7),status=1, editor_reviewed=1).order_by(total_view='DESC')
    
    def resolve_last_month_popular_article(self, info, **kwargs):
        return Article.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=30),status=1, editor_reviewed=1)
    
    def resolve_popular_article_by_category_last_month(self, info, category_uId, **kwargs):
        if category_uId is not None:
            obj = Article.objects.filter(category__uniqueId=category_uId, status=1, editor_reviewed=1).order_by(total_view='DESC')[:10]
            return obj
     
    def resolve_popular_article_by_writter(self, info, writter_uId, **kwargs):
        if writter_uId is not None:
            obj = Article.objects.filter(writter__uniqueId=writter_uId, status=1, editor_reviewed=1).order_by(total_view='DESC')[:10]
            return obj
    
    def resolve_related_article_by_category_last_month(self, info, category_uId, **kwargs):
        if category_uId is not None:
            obj = Article.objects.filter(category__uniqueId=category_uId, status=1, editor_reviewed=1).order_by(total_view='DESC')[:10]
            return obj
        return None
    
    def resolve_related_article_by_writter_last_ten(self, info, writter_uId, **kwargs):
        if writter_uId is not None:
            obj = Article.objects.filter(writter__uniqueId=writter_uId, status=1, editor_reviewed=1).order_by(total_view='DESC')[:10]
            return obj
        return None

class Mutation(graphene.ObjectType):
    pass   
    
schema = graphene.Schema(query=Query, mutation=Mutation)
