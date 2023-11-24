from django.contrib import admin
from feature.models import *
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *
from django.conf import settings
class FeatureAdmin(ImportExportModelAdmin):
    resource_class = FeatureResource

class FeatureCategoryAdmin(ImportExportModelAdmin):
    resource_class = FeatureCategoryResource

class FeaturePostAdmin(ImportExportModelAdmin):
    resource_class = FeaturePostResource

# Register your models here.
# admin.site.register(Feature, FeatureAdmin)
# admin.site.register(FeatureCategory, FeatureCategoryAdmin)
# admin.site.register(FeaturePost, FeaturePostAdmin)

if settings.DEBUG: 
    admin.site.register(Feature, FeatureAdmin)
    admin.site.register(FeatureCategory, FeatureCategoryAdmin)
    admin.site.register(FeaturePost, FeaturePostAdmin)
else:
    admin.site.register(Feature)
    admin.site.register(FeatureCategory)
    admin.site.register(FeaturePost)
