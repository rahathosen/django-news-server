from django.contrib import admin
from django.urls import include, path

# For static files
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# For GraphQL
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from homepage.views import index
from .sitemap import sitemapUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True)))   
]
urlpatterns += sitemapUrl
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += [
        path('', index),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to Portal Admin Panel"