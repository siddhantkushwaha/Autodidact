from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app:home'))
    return render(request, 'index.html')


# def signUpUser(request):
#     logout(request)
#     if request.POST:
#         print(request.POST)
#         form = SignUpForm(request.POST)
#         print(form)
#         if form.is_valid():
#             new_user = User.objects.create_user(**form.cleaned_data)
#             new_forum_user = ForumUser()
#             new_forum_user.user = new_user
#             new_forum_user.save()
#             login(request, new_user)
#             return HttpResponseRedirect(reverse('app:home'))
#     else:
#         form = SignUpForm()
#
#     return render(request, 'signup.html', {'form': form})


def logInUser(request):
    # logout(request)
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = authenticate(username=username, password=password)
        user = authenticate(request, username, password)
        print(type)
        user_id = 1234;
        if user_id is not None:
            # login(request, user)
            user = User()

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


@login_required
def posts(request):
    template = 'posts.html'
    context = {
             'user':request.user,
    }
    return render(request, template, context)

@login_required
def tags(request):
    template = 'tags.html'
    context = {
             'user':request.user,
    }
    return render(request, template, context)

@login_required
def users(request):
    template = 'users.html'
    context = {
             'user':request.user,
    }
    return render(request, template, context)

@login_required
def userDetails(request):
    template = 'profile.html'
    context = {
             'user':request.user,
    }
    return render(request, template, context)
