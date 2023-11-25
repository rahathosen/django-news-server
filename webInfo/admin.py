from django.contrib import admin
from webInfo.models import *
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *
from django.conf import settings

class WebsiteInfoAdmin(ImportExportModelAdmin):
    resource_class = WebsiteInfoResource

class NavigationAdmin(ImportExportModelAdmin):
    resource_class = NavMenuResource

class PollAdmin(ImportExportModelAdmin):
    resource_class = PollResource

# Register your models here.
# admin.site.register(WebsiteInfo, WebsiteInfoAdmin)
# admin.site.register(Navigation, NavigationAdmin)
# admin.site.register(Poll, PollAdmin)
# admin.site.register(HeadLine)
# admin.site.register(BreakingNews)
# admin.site.register(HeadNews)
# admin.site.register(HomeHighlightedNews)
# admin.site.register(SectionBox)

if settings.DEBUG: 
    admin.site.register(WebsiteInfo, WebsiteInfoAdmin)
    admin.site.register(Navigation, NavigationAdmin)
    admin.site.register(Poll, PollAdmin)
    admin.site.register(HeadLine)
    admin.site.register(BreakingNews)
    admin.site.register(HeadNews)
    admin.site.register(HomeHighlightedNews)
    admin.site.register(SectionBox)
else:
    admin.site.register(WebsiteInfo)
    admin.site.register(Navigation)
    # admin.site.register(Poll)
    admin.site.register(HeadLine)
    admin.site.register(BreakingNews)
    admin.site.register(HeadNews)
    admin.site.register(HomeHighlightedNews)
    admin.site.register(SectionBox)







