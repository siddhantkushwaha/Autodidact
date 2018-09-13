from django.conf.urls import url

from app import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^signup$', views.signUpUser, name='signup'),
    url(r'^login$', views.logInUser, name='login'),
    url(r'^home$', views.home, name='home'),
]
