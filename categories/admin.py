from django.contrib import admin
from categories.models import *
# Register your export resource models here.
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *
# Register your models here.

class PostCategoryAdmin(ImportExportModelAdmin):
    resource_class = PostCategoryResource

class PostSubCategoryAdmin(ImportExportModelAdmin):
    resource_class = PostSubCategoryResource

class PostTagAdmin(ImportExportModelAdmin):
    resource_class = PostTagResource

class ContinentAdmin(ImportExportModelAdmin):
    resource_class = ContinentResource

class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource

class DivisionAdmin(ImportExportModelAdmin):
    resource_class = DivisionResource

class DistrictAdmin(ImportExportModelAdmin):
    resource_class = DistrictResource

class CityCorporationAdmin(ImportExportModelAdmin):
    resource_class = CityCorporationResource

class UpozilaAdmin(ImportExportModelAdmin):
    resource_class = UpozilaResource

class PourosavaAdmin(ImportExportModelAdmin):
    resource_class = PourosavaResource

class ThanaAdmin(ImportExportModelAdmin):
    resource_class = ThanaResource

class UnionAdmin(ImportExportModelAdmin):
    resource_class = UnionResource

class ZipPostalCodeAdmin(ImportExportModelAdmin):
    resource_class = ZipPostalCodeResource

class TurisumSpotAdmin(ImportExportModelAdmin):
    resource_class = TurisumSpotResource

admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(CityCorporation, CityCorporationAdmin)
admin.site.register(Upozila, UpozilaAdmin)
admin.site.register(Union, UnionAdmin)
admin.site.register(Thana, ThanaAdmin)
admin.site.register(Pourosava, PourosavaAdmin)
admin.site.register(ZipPostalCode, ZipPostalCodeAdmin)
admin.site.register(TurisumSpot, TurisumSpotAdmin)

admin.site.register(NewsCategory, PostCategoryAdmin)
admin.site.register(NewsSubCategory, PostSubCategoryAdmin)
admin.site.register(PostsTag, PostTagAdmin)