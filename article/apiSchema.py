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
    articles = graphene.List(ArticleType, first = graphene.Int(), skip = graphene.Int())
    article = graphene.Field(ArticleType, id=graphene.Int())
    article_categories = graphene.List(ArticleCategoryType, first = graphene.Int(), skip = graphene.Int())
    article_category = graphene.Field(ArticleCategoryType, id=graphene.Int())
    article_writters = graphene.List(ArticleWritterType, first = graphene.Int(), skip = graphene.Int())
    article_writter = graphene.Field(ArticleWritterType, id=graphene.Int())

    today_articles = graphene.List(ArticleType)
    last_week_popular_article  = graphene.List(ArticleType)
    last_month_popular_article = graphene.List(ArticleType)

    popular_article_by_category_last_month = graphene.List(ArticleType, category_id=graphene.Int())
    popular_article_by_writter = graphene.List(ArticleType, writter_id=graphene.Int())

    related_article_by_category_last_month = graphene.List(ArticleType, category_id=graphene.Int())
    related_article_by_writter_last_ten = graphene.List(ArticleType, writter_id=graphene.Int())


    def resolve_articles(self, info, first=None, skip=None, **kwargs):
        articles = Article.objects.all()
        if skip:
            articles = articles[skip:]
        if first:
            articles = articles[:first]

        return articles
    
    def resolve_article(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = Article.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_article_categories(self, info, first=None, skip=None, **kwargs):
        article_categories = ArticleCategory.objects.all()
        if skip:
            article_categories = article_categories[skip:]
        if first:
            article_categories = article_categories[:first]

        return article_categories
    
    def resolve_article_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = ArticleCategory.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_article_writters(self, info, first=None, skip=None, **kwargs):
        article_writters = ArticleWritter.objects.all()
        if skip:
            article_writters = article_writters[skip:]
        if first:
            article_writters = article_writters[:first]

        return article_writters
    
    def resolve_article_writter(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            obj = ArticleWritter.objects.get(pk=id)
            obj.total_view = obj.total_view + 1
            obj.save()
            return obj
        return None
    
    def resolve_today_articles(self, info, **kwargs):
        return Article.objects.filter(created_at__date=datetime.date.today()).order_by(total_view='DESC')
    
    def resolve_last_week_popular_article(self, info, **kwargs):
        return Article.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=7)).order_by(total_view='DESC')
    
    def resolve_last_month_popular_article(self, info, **kwargs):
        return Article.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=30)).order_by(total_view='DESC')
    
    def resolve_popular_article_by_category_last_month(self, info, category_id, **kwargs):
        return Article.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=30), category_id=category_id).order_by(total_view='DESC')
    
    def resolve_popular_article_by_writter(self, info, writter_id, **kwargs):
        return Article.objects.filter(writter_id=writter_id).order_by(total_view='DESC')
    
    def resolve_related_article_by_category_last_month(self, info, category_id, **kwargs):
        return Article.objects.filter(created_at__gte=datetime.date.today()-datetime.timedelta(days=30), category_id=category_id).order_by(total_view='DESC')[:10]
    
    def resolve_related_article_by_writter_last_ten(self, info, writter_id, **kwargs):
        return Article.objects.filter(writter_id=writter_id).order_by(total_view='DESC')[:10]

class Mutation(graphene.ObjectType):
    pass   
    
schema = graphene.Schema(query=Query, mutation=Mutation)

# Test Query
# Test article query
# query {
#   articles {
#     id
#     title
#     category {
#       id
#       name
#     }
#     writter {
#       id
#       name
#     }
#     totalView
#     createdAt
#   }

#   article(id: 1) {
#     id
#     title
#     category {
#       id
#       name
#     }
#     writter {
#       id
#       name
#     }
#     totalView
#     createdAt
#   }
# }

# Test article category query
# query {
#   articleCategories {
#     id
#     name
#     totalView
#     createdAt
#   }

#   articleCategory(id: 1) {
#     id
#     name
#     totalView
#     createdAt
#   }
# }

# Test article writter query
# query {
#   articleWritters {
#     id
#     name
#     totalView
#     createdAt
#   }

#   articleWritter(id: 1) {
#     id
#     name
#     totalView
#     createdAt
#   }
# }

# Test today article query
# query {
#   todayArticles {
#     id
#     title
#     category {
#       id
#       name
#     }
#     writter {
#       id
#       name
#     }
#     totalView
#     createdAt
#   }
# }

# Test last week popular article query
# query {
#   lastWeekPopularArticle {
#     id
#     title
#     category {
#       id
#       name
#     }
#     writter {
#       id
#       name
#     }
#     totalView
#     createdAt
#   }
# }

# Test last month popular article query
# query {
#   lastMonthPopularArticle {
#     id
#     title
#     category {
#       id
#       name
#     }
#     writter {
#       id
#       name
#     }
#     totalView
#     createdAt
#   }
# }

# Test popular article by category last month query
# query {
#   popularArticleByCategoryLastMonth(categoryId: 1) {
#     id    
#     title
#     category {
#       id
#       name    
#     }
#     writter {
#       id
#       name
#     }
#     totalView
#     createdAt
#   }
# }

# Test popular article by writter query
# query {
#   popularArticleByWritter(writterId: 1) {
#     id
#     title
#     category {
#       id
#       name
#     }
#     writter {
#       id
#       name
#     }
#     totalView
#     createdAt
#   }   
# } 

# Test related article by category last month query
# query {
#   relatedArticleByCategoryLastMonth(categoryId: 1) {
#     id
#     title
#     category {
#       id
#       name
#     }
#     writter {
#       id
#       name
#     }
#     totalView
#     createdAt
#   }
# }

# Test related article by writter last ten query
# query {
#   relatedArticleByWritterLastTen(writterId: 1) {
#     id
#     title
#     category {
#       id
#       name
#     }
#     writter {
#       id
#       name
#     }
#     totalView
#     createdAt
#   }
# }
