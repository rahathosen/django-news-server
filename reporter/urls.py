from django.urls import path
from reporter import views


urlpatterns = [
    path('', views.index, name='index'),
]