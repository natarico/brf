from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sign_up, name='sign_up'),
    url(r'^signup/$', views.sign_up, name='sign_up'),
    url(r'^survey/$', views.survey, name='survey'),
    url(r'^dashboard/$', views.dashboard, name='dash'),
    url(r'^profile/$', views.profile, name='profile'),
    

]