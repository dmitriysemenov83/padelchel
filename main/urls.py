from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('more/', views.more, name='more'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),

    path('sitemap.xml', TemplateView.as_view(
        template_name='main/sitemap.xml',
        content_type='application/xml'), name='sitemap'),

    path('robots.txt', views.robots_txt, name='robots_txt'),
]