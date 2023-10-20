from django.contrib import admin
from article.models import *

# Register your export resource models here.
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *
class ArticleAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource

class ArticleCategoryAdmin(ImportExportModelAdmin):
    resource_class = ArticleCategoryResource

class ArticleWritterAdmin(ImportExportModelAdmin):
    resource_class = ArticleWritterResource
# Register your models here.
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(ArticleWritter, ArticleWritterAdmin)
admin.site.register(Article, ArticleAdmin)
