from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^addTag$', views.addTag, name='addTag')
]
