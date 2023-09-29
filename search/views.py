from django.shortcuts import render
from search.models import *
from news.models import *
from article.models import *
from reporter.models import *
from categories.models import *

from django.db.models import Q

from pyuca import Collator

def fullTextSearch(request):
    article_list = sorted(Article.objects.all(), key=lambda x: (Collator().sort_key, x.lastname, x.firstname))
    post_list = sorted(Post.objects.all(), key=lambda x: (Collator().sort_key, x.lastname, x.firstname))