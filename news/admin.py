from django.contrib import admin
from news.models import *
from import_export.admin import ImportExportModelAdmin
from webInfo.resources import *
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

# VIEW_TOTAL_VIEW_PERMISSION = Permission(
#     name="Can view total view",
#     content_type=ContentType.objects.get_for_model(Post),
#     codename="view_total_view",
# )

# # Create the "Superusers" group if it doesn't exist
# try:
#     Group.objects.get(name="Editors")
# except Group.DoesNotExist:
#     user_group = Group(name="Editors")
#     user_group.save()

class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource

class PostAdminExclude(admin.ModelAdmin):
    search_fields = ['title', 'description', 'details']
    exclude = ('total_view',)

    # def has_view_permission(self, request):
    #     # Check if the user is a superuser
    #     if request.user.is_superuser:
    #         return True

    #     # Check if the user has the "Can view total view" permission
    #     if request.user.has_perm('news.view_total_view'):
    #         return True

    #     # If the user does not have the permission, hide the 'total_view' field
    #     self.list_display.remove('total_view')  
    #     return True


# Register your models here.
# admin.site.register(Post, PostAdminExclude)

if settings.DEBUG: 
    admin.site.register(Post, PostAdmin)
else:
    admin.site.register(Post, PostAdminExclude)