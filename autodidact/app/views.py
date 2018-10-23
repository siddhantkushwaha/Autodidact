from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.forms import LoginForm
from app.models import *


def index(request):
    template = 'index.html'
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:home'))
    return render(request, template)


def login_user(request):
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
        'posts': Thread.objects.order_by('-id')[:6],
        'tags': Tag.objects.order_by('-id')[:6]
    }
    return render(request, template, context)


@login_required
def get_posts(request):
    template = 'posts.html'
    items_per_page = 25
    page = int(request.GET.get(key='page', default=1))

    posts = Thread.objects.all()
    paginator = Paginator(object_list=posts, per_page=items_per_page)

    context = {
        'user': request.user,
        'items': paginator.page(page),
    }
    return render(request, template, context)


@login_required
def get_tags(request):
    template = 'tags.html'
    items_per_page = 25
    page = int(request.GET.get(key='page', default=1))

    tags = Tag.objects.order_by('use_count').order_by('id')
    paginator = Paginator(object_list=tags, per_page=items_per_page)

    context = {
        'user': request.user,
        'items': paginator.page(page),
    }
    return render(request, template, context)


@login_required
def users(request):
    template = 'users.html'
    items_per_page = 25
    page = int(request.GET.get(key='page', default=1))

    forumUsers = ForumUser.objects.order_by('reputation')
    paginator = Paginator(object_list=forumUsers, per_page=items_per_page)

    context = {
        'user': request.user,
        'items': paginator.page(page),
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

    try:
        ForumUser.objects.get(django_user=user)
    except Exception as e:
        print(e)
        forum_user = ForumUser()
        forum_user.django_user = user
        forum_user.save()

    user = authenticate(username=email, password=password)
    return user


@login_required
def add_tag(request):
    if request.POST:
        tag_name = request.POST.get('tag')

        cursor = connection.cursor()
        forum_user_id = ForumUser.objects.get(django_user=request.user).id

        query = 'call add_tag("%s", %d)' % (tag_name, forum_user_id)
        cursor.execute(query)

        return HttpResponseRedirect(reverse('app:main'))
    else:
        return HttpResponse('This is a get request.')

@login_required
def add_post(request):
    if request.POST:
        print(request.POST)
        title = request.POST.get('title')
        description = request.POST.get('editor1')

        cursor = connection.cursor()
        query = 'call add_post("%s","%s", %d)' % (title,description, ForumUser.objects.get(django_user=request.user).id)
        print(query)
        cursor.execute(query)

        return HttpResponseRedirect(reverse('app:main'))
    else:
        return HttpResponse('This is a get request.')
