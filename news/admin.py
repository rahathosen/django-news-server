from django.contrib import admin
from news.models import *
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *

class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource


# Register your models here.
admin.site.register(Post, PostAdmin)