from django.conf.urls import url
from django.contrib.auth.views import logout

from app import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^home$', views.home, name='home'),
    url(r'^posts$', views.posts, name='posts'),
    url(r'^tags$', views.tags, name='tags'),
    url(r'^users$', views.users, name='users'),
    url(r'^userDetails$', views.user_details, name='userDetails'),
    url(r'^add/tag$', views.add_tag, name='addTag'),

    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]
