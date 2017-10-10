from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
import bcrypt

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        print "did we get here1"
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print "did we get here2"
            password = bcrypt.hashpw(request.POST["password1"].encode(), bcrypt.gensalt())
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            login(request, user)
            print "did we get here3"
            return redirect(reverse('survey'))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def survey(request):
    return render(request, 'survey.html')

