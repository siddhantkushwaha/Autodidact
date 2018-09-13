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
        print(request.POST)
        form = SignUpForm(request.POST)
        print(form)
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
    print("doing login-1")
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username + " " + password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('app:home'))
        else:
            return HttpResponse('error login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def home(request):
    template = 'home.html'
    context = {
             'user':request.user,
    }
    return render(request, template, context)

# macrosensors=MacroSensor.objects.all()
#     template = 'sensors/macro.html'
#     context={
#         'macrosensors':macrosensors,
#         'user':request.user,
#     }
#     return render(request,template,context)
