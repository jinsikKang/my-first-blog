#_*_coding:utf-8_*_
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^add_post/$', views.write_post, name='write_post'),
]