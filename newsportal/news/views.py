from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html', context={'posts': posts})


def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'detail.html', context={'post': post})


class Posts(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']
    paginate_by = 2