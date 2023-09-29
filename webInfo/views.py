from django.shortcuts import render
from webInfo.models import *

def index(request):
    websiteInfo = WebsiteInfo.objects.last()
   
    context = {
        'appName': 'Info App',
        'websiteInfo': websiteInfo,
    }
    return render(request, 'index.html', context)

