from django.contrib import admin
from webInfo.models import *
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *

class WebsiteInfoAdmin(ImportExportModelAdmin):
    resource_class = WebsiteInfoResource

class NavigationAdmin(ImportExportModelAdmin):
    resource_class = NavMenuResource

class HeadLineAdmin(ImportExportModelAdmin):
    resource_class = HeadLineResource

class BreakingNewsAdmin(ImportExportModelAdmin):
    resource_class = BreakingNewsResource

class CoverAdmin(ImportExportModelAdmin):
    resource_class = CoverResource

class SectionBoxAdmin(ImportExportModelAdmin):
    resource_class = SectionResource

class PollAdmin(ImportExportModelAdmin):
    resource_class = PollResource


# Register your models here.
admin.site.register(WebsiteInfo, WebsiteInfoAdmin)
admin.site.register(Navigation, NavigationAdmin)
admin.site.register(HeadLine, HeadLineAdmin)
admin.site.register(BreakingNews, BreakingNewsAdmin)
admin.site.register(Cover, CoverAdmin)
admin.site.register(SectionBox, SectionBoxAdmin)
admin.site.register(Poll, PollAdmin)





