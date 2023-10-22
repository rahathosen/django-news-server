from django.contrib import admin
from feature.models import *
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *

class FeatureAdmin(ImportExportModelAdmin):
    resource_class = FeatureResource

class FeatureCategoryAdmin(ImportExportModelAdmin):
    resource_class = FeatureCategoryResource

class FeaturePostAdmin(ImportExportModelAdmin):
    resource_class = FeaturePostResource

# Register your models here.
admin.site.register(Feature, FeatureAdmin)
admin.site.register(FeatureCategory, FeatureCategoryAdmin)
admin.site.register(FeaturePost, FeaturePostAdmin)
