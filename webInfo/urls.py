from django.urls import path
from webInfo import views


urlpatterns = [
    path('', views.index, name='index'),
]