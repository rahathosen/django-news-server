from django.contrib import admin
from advertisement.models import *
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *
from django.conf import settings

class AdBoxAdmin(ImportExportModelAdmin):
    resource_class = AdBoxResource

class AdCompanyAdmin(ImportExportModelAdmin):
    resource_class = AdCompanyResource

class AdvertisementAdmin(ImportExportModelAdmin):
    resource_class = AdvertisementResource
# Register your models here.
# admin.site.register(AdBox, AdBoxAdmin)
# admin.site.register(AdCompany, AdCompanyAdmin)
# admin.site.register(Advertisement, AdvertisementAdmin)

class AdminExclude(admin.ModelAdmin):
    search_fields = ['title', 'uniqueId']
    exclude = ('total_view',)

if settings.DEBUG: 
    admin.site.register(AdBox, AdBoxAdmin)
    admin.site.register(AdCompany, AdCompanyAdmin)
    admin.site.register(Advertisement, AdvertisementAdmin)
else:
    admin.site.register(AdBox, AdminExclude)
    admin.site.register(AdCompany, AdminExclude)
    admin.site.register(Advertisement, AdminExclude)