from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.heal, name='healup'),
    url(r'^hospital/$', views.hospital, name='hospital'),
    url(r'^arcade/', views.arcade, name='arcade'),
    url(r'^pacman/', views.pacman, name='pacman'),
]
