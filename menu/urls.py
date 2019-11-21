from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('menus/new', views.nuevo_menu, name='nuevo_menu'),
]