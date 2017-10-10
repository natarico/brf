from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def sign_up(request):
    form = UserCreationForm(request.POST)
    return render(request, 'signup.html', {'form': form})
