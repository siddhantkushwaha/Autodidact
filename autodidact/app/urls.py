from django.conf.urls import url
from django.contrib.auth.views import logout

from app import views

app_name = 'app'

urlpatterns = [

    url(r'^$', views.main, name='main'),                                            # View the index page of the discussion forum
    url(r'^login/(?P<token>.+)$', views.login_user, name='login'),                  # Login to the discussion Forum
    url(r'^profile$', views.user_profile, name='userProfile'),                      # View your profile on the forum

    url(r'^posts$', views.get_posts, name='posts'),
    url(r'^tags$', views.get_tags, name='tags'),
    url(r'^users$', views.get_users, name='users'),                                 # View all the posts/tags/users created on the forum

    url(r'^post/details/(?P<pk>[0-9]+)$', views.post_details, name='postDetails'),
    url(r'^tag/details/(?P<pk>[0-9]+)$', views.tag_details, name='tagDetails'),
    url(r'^user/details/(?P<pk>[0-9]+)$', views.user_details, name='userDetails'),  # View all detailed page of a post/tag/user created on the forum

    url(r'^add/tag$', views.add_tag, name='addTag'),
    url(r'^add/post$', views.add_post, name='addPost'),
    url(r'^add/answer$', views.add_answer, name='addAnswer'),
    url(r'^add/comment$', views.add_comment, name='addComment'),                    # Adding a tag/post/answer/comment on the forum

    url(r'^update/tag$', views.update_tag, name='updateTag'),                       # Update title of an existing Tag

    url(r'^search/tags$', views.search_tags, name='searchTags'),                    # Search for tags while Asking a Question

    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),                    # Logging out a User
]
