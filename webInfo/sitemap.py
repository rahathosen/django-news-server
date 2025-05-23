from django.contrib.sitemaps import Sitemap
from news.models import *
from article.models import *
from categories.models import *
from reporter.models import *
from search.models import *
from webInfo.models import *
from feature.models import *

class NewsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5
    def items(self):
        return Post.objects.filter(status=1, editor_reviewed=1).order_by('-created_at')
    
    def location(self, obj):
        return f"/{obj.uniqueId}/"
    
    def lastmod(self, obj):
        return obj.updated_at
    
class ArticleSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.9
    def items(self):
        return Article.objects.filter(status=1, editor_reviewed=1).order_by('-created_at')
    
    def location(self, obj):
        return f"/{obj.uniqueId}/"
    
    def lastmod(self, obj):
        return obj.updated_at
    
class FeaturePostSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 1
    def items(self):
        return FeaturePost.objects.filter(status=1, editor_reviewed=1).order_by('-created_at')
    
    def location(self, obj):
        return f"/{obj.uniqueId}/"
    
    def lastmod(self, obj):
        return obj.updated_at


sitemaps = {
'Post': NewsSitemap(),
'Article': ArticleSiteMap(),
'Feature': FeaturePostSiteMap()
}

from django.contrib.sitemaps.views import sitemap
from django.urls import path

sitemapUrl = [
    path('sitemap', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]