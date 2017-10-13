from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^end/', views.endgame, name='endgame'),
    url(r'^healed/', views.healed, name='healed'),
]
