from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^arcade/', views.arcade, name='arcade'),
    url(r'^pacman/', views.pacman, name='pacman'),
]
