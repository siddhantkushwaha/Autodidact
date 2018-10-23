from django.conf.urls import url
from django.contrib.auth.views import logout

from app import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^home$', views.home, name='home'),
    url(r'^posts$', views.get_posts, name='posts'),
    url(r'^tags$', views.get_tags, name='tags'),
    url(r'^users$', views.get_users, name='users'),
    url(r'^user/profile$', views.user_profile, name='userProfile'),
    url(r'^add/tag$', views.add_tag, name='addTag'),
    url(r'^add/post$', views.add_post, name='addPost'),
    url(r'^tag/details$', views.tag_details, name='tagDetails'),
    url(r'^user/details$', views.user_details, name='userDetails'),

    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]
