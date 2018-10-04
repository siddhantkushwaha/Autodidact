from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.forms import LoginForm


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:home'))
    return render(request, 'index.html')


def logInUser(request):
    logout(request)
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        user = stub_auth(email, password)

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
        'user': request.user,
    }
    return render(request, template, context)


@login_required
def posts(request):
    template = 'posts.html'
    context = {
        'user': request.user,
    }
    return render(request, template, context)


@login_required
def tags(request):
    template = 'tags.html'
    context = {
        'user': request.user,
    }
    return render(request, template, context)


@login_required
def users(request):
    template = 'users.html'
    context = {
        'user': request.user,
    }
    return render(request, template, context)


@login_required
def userDetails(request):
    template = 'profile.html'
    context = {
        'user': request.user,
    }
    return render(request, template, context)


def stub_auth(email, password):
    user_dict = {
        'siddhant.k16@iiits.in': 'siddhant@1234',
        'prakkash.m16@iiits.in': 'prakkash@1234',
        'udayraj.s16@iiits.in': 'udayraj@1234'
    }

    if email not in user_dict.keys():
        return None

    if user_dict[email] != password:
        return None

    username = 'autodidact_user'
    password = 'user@2018'
    user = authenticate(username=username, password=password)
    return user

# def get_session_user():
    
