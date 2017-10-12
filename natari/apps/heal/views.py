from django.shortcuts import render
from ..play.models import *
import time

# Create your views here.
def arcade(request):
    return render(request, 'heal/arcade.html')

def pacman(request):
    return render(request, 'pacman.html')

# def countdown(request):
#     bars = GameStats.objects.get(user=request.user).health
#     for i in range(60, 0):
#         time.wait(1)
#         ctdn = i
#     msg = 'You have earned {} health bars!'.format(morebar)
