from django.contrib import admin
from article.models import *
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *
from django.conf import settings

class ArticleAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource

class ArticleCategoryAdmin(ImportExportModelAdmin):
    resource_class = ArticleCategoryResource

class ArticleWritterAdmin(ImportExportModelAdmin):
    resource_class = ArticleWritterResource
    
# Register your models here.
# admin.site.register(ArticleCategory, ArticleCategoryAdmin)
# admin.site.register(ArticleWritter, ArticleWritterAdmin)
# admin.site.register(Article, ArticleAdmin)

if settings.DEBUG: 
    admin.site.register(ArticleCategory, ArticleCategoryAdmin)
    admin.site.register(ArticleWritter, ArticleWritterAdmin)
    admin.site.register(Article, ArticleAdmin)
else:
    admin.site.register(ArticleCategory)
    admin.site.register(ArticleWritter)
    admin.site.register(Article)