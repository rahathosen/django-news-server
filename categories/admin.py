from django.contrib import admin
from categories.models import *
# Register your models here.
class PostsTagAdmin(admin.ModelAdmin):
    list_display = ('title', 'serial', 'sortDetails')
    list_filter = ("serial",)
    search_fields = ['title', 'sortDetails']
    prepopulated_fields = {'url': ('url',)}
admin.site.register(PostsTag, PostsTagAdmin)

admin.site.register(Continents)
admin.site.register(Country)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(CityCorporation)
admin.site.register(Upozila)
admin.site.register(Union)
admin.site.register(Thana)
admin.site.register(Pourosava)
admin.site.register(ZipPostalCode)

admin.site.register(NewsCategory)
admin.site.register(NewsSubCategory)
admin.site.register(TurisumSpot)