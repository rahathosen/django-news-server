from django.urls import path
from categories import views


urlpatterns = [
    path('', views.index, name='index'),
]