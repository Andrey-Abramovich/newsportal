from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView
from .filters import PostFilter

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
    paginate_by = 3

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'filter': self.get_filter(),
        }