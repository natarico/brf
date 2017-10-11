from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import *
from .models import *
import bcrypt
import requests

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password = bcrypt.hashpw(request.POST["password1"].encode(), bcrypt.gensalt())
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            login(request, user)
            return redirect(reverse('survey'))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def survey(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = User.objects.get(id = request.user.id)
            profile.city = form.cleaned_data.get('city')
            profile.weather = form.cleaned_data.get('weather')
            profile.save()
            return redirect(reverse('dash'))
    else:
        form = ProfileForm()
    return render(request, 'survey.html', {'form': form})

def dashboard(request):
    context = {
        'users_online' : User.objects.all(),
        'high_scores' : User.objects.all().order_by("-profile__high_score")[:3]
    }
    return render(request, 'home.html', context)

def profile(request):
    return render(request, 'profile.html')

def hospital(request):
    # url = 'http://api.openweathermap.org/data/2.5/weather?q=Seattle'
    # r = requests.get(url)
    # print r
    return render(request, 'hospital.html')
