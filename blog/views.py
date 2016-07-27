#_*_coding:utf-8_*_

from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def write_post(request):
    me = User.objects.get(username='jskang')
    title = request.GET['title' ]
    text  = request.GET['text'  ]
    post = Post.objects.create(author=me, title=title, text=text)
    post.publish()
    return render(request, 'blog/post_list.html', {})