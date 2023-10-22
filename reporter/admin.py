from django.contrib import admin
from reporter.models import *
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *

class ReporterAdmin(ImportExportModelAdmin):
    resource_class = ReporterResource
# Register your models here.
admin.site.register(Reporter, ReporterAdmin)