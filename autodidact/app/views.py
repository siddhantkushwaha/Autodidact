from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from app.forms import *


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:home'))
    return render(request, 'index.html')


def signUpUser(request):
    logout(request)
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_forum_user = ForumUser()
            new_forum_user.user = new_user
            new_forum_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('app:home'))
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def logInUser(request):
    logout(request)
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('app:home'))
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')
