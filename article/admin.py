from django.contrib import admin
from article.models import *
# Register your models here.
admin.site.register(ArticleCategory)
admin.site.register(ArticleWritter)
admin.site.register(Article)
