from django.contrib import admin
from news.models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'status', 'created_at')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'url': ('url',)}

admin.site.register(Post, PostAdmin)


