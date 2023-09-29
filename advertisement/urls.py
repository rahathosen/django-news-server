from django.urls import path
from advertisement import views


urlpatterns = [
    path('', views.index, name='index'),
]