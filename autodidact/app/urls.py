from django.conf.urls import url
from django.contrib.auth.views import logout

from app import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    # url(r'^login$', views.login_user, name='login'),
    url(r'^(?P<token>[0-9]+)$', views.login_user, name='login'),
    url(r'^profile$', views.user_profile, name='userProfile'),

    url(r'^posts$', views.get_posts, name='posts'),
    url(r'^tags$', views.get_tags, name='tags'),
    url(r'^users$', views.get_users, name='users'),

    url(r'^post/details/(?P<pk>[0-9]+)$', views.post_details, name='postDetails'),
    url(r'^tag/details/(?P<pk>[0-9]+)$', views.tag_details, name='tagDetails'),
    url(r'^user/details/(?P<pk>[0-9]+)$', views.user_details, name='userDetails'),

    url(r'^add/tag$', views.add_tag, name='addTag'),
    url(r'^add/post$', views.add_post, name='addPost'),
    url(r'^add/answer$', views.add_answer, name='addAnswer'),
    url(r'^add/comment$', views.add_comment, name='addComment'),

    url(r'^update/tag$', views.update_tag, name='updateTag'),

    url(r'^search/tags$', views.search_tags, name='searchTags'),

    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]
