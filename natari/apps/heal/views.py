# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import *
from ..brf.models import *
from django.contrib.auth import login, authenticate
import requests

# Create your views here.

def heal(request):
    return render(request, 'heal/heal.html')

def hospital(request):
    user = User.objects.get(id = request.user.id)
    city = user.profile.city
    print city
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + "city" + '&APPID=4b371518238f96076fa4f1230f047d25'
    response = requests.get(url)
    data = response.json()
    print data
    id = data['weather'][0]['id']
    # id = 952
    print id
    if 300 <= id <= 531 or id == 701 or id == 741:
        print "it's rainy!"
        weather = [1, "rainy"]
    if 200 <= id <= 232 or 900 <= id <= 906 or 956 <= id <= 962 or 711 <= id <= 731 or 751 <= id <= 781:
        print "it's stormy!"
        weather = [5, "stormy"]
    if 951 <= id <= 955 or id == 800:
        print "it's sunny!"
        weather = [2, "sunny"]
    if 600 <= id <= 622:
        print "it's snowy!"
        weather = [3, "snow"]
    if 801 <= id <= 804:
        print "it's cloudy!"
        weather = [4, "cloudy"]
    if user.profile.weather == weather[0]:
        pace = "faster"
    else:
        pace = "slower"
    player = GameStats.objects.get(user=request.user)
    context = {
        'player': player,
        'city': city,
        'weather' : weather[1],

    }
    print pace
    return render(request, 'heal/hospital.html', context)

def arcade(request):
    return render(request, 'heal/arcade.html')
