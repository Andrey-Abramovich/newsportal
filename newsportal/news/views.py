from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})


def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'detail.html', context={'post': post})

