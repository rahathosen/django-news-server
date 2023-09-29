from django.contrib.sitemaps import Sitemap
from news.models import *
from advertisement.models import *
from article.models import *
from categories.models import *
from reporter.models import *
from search.models import *
from webInfo.models import *

class NewsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5
    def items(self):
        return Post.objects.filter(status=1).order_by('-created_at')
    
    def location(self, obj):
        return f"/{obj.pk}/"
    
    def lastmod(self, obj):
        return obj.updated_at.filter(status=1).order_by('-created_at')
    

sitemaps = {
'Post': NewsSitemap()
}

from django.contrib.sitemaps.views import sitemap
from django.urls import path

sitemapUrl = [
    path('sitemap', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]