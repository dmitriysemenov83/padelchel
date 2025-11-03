from django.urls import path
from . import views
from .views import tournaments

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('more/', views.more, name='more'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]