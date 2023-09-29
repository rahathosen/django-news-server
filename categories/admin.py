from django.contrib import admin
from categories.models import *
# Register your models here.
# admin.site.register(Language)
admin.site.register(Continents)
admin.site.register(Country)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Upozila)
admin.site.register(CityCorporation)
admin.site.register(NewsCategory)
admin.site.register(NewsSubCategory)

class PostsTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'serial', 'sortDetails')
    list_filter = ("serial",)
    search_fields = ['title', 'sortDetails']
    prepopulated_fields = {'url': ('url',)}
admin.site.register(PostsTag, PostsTagAdmin)