from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.forms import LoginForm
from app.models import ForumUser


def index(request):
    template = 'index.html'
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:home'))
    return render(request, template)


def logInUser(request):
    logout(request)

    template = 'login.html'
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        user_id, user = stub_auth(email, password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('app:home'))
        else:
            return HttpResponse('error login')
    else:
        form = LoginForm()

    return render(request, template, {'form': form})


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
def user_details(request):
    template = 'profile.html'
    context = {
        'user': request.user,
    }
    return render(request, template, context)


def stub_auth(email, password):
    if email == '' or password == '':
        return None, None

    user_dict = {
        'siddhant.k16@iiits.in': {'password': 'siddhant@1234', 'id': 1},
        'prakkash.m16@iiits.in': {'password': 'prakkash@1234', 'id': 2},
        'udayraj.s16@iiits.in': {'password': 'uday@1234', 'id': 3},
    }

    if email not in user_dict.keys():
        return None, None

    if user_dict[email]['password'] != password:
        return None, None

    user_id = user_dict[email]['id']
    return user_id, get_forum_user(email, password)


def get_forum_user(email, password):
    try:
        user = User.objects.get(username=email)
    except Exception as e:
        print(e)
        user = User()
        user.username = email
        user.email = email
        user.set_password(password)
        user.save()

        forum_user = ForumUser()
        forum_user.django_user = user
        forum_user.save()

    user = authenticate(username=email, password=password)
    return user

# def get_forum_user(email, p)

@login_required
def add_tag(request):
    if request.POST:
        tag = request.POST.get('tag')

        print(tag)
        print(ForumUser.objects.get(django_user=request.user))

        return HttpResponse('Done')
    else:
        return HttpResponse('This is a get request.')