from .models import *
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin


# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html', context={'posts': posts})


# def detail(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'detail.html', context={'post': post})

# class IndexView(LoginRequiredMixin, TemplateView):
#     model = Post
#     template_name = 'news/template/news/index.html'
#     context_object_name = 'posts'
#     ordering = ['-dateCreation']
#     paginate_by = 10
#
#     def get_filter(self):
#         return PostFilter(self.request.GET, queryset=super().get_queryset())
#
#     def get_queryset(self):
#         return self.get_filter().qs
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
#         return context


class Posts(ListView):
    model = Post

    template_name = 'news/template/news/index.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']
    paginate_by = 10
    # form_class = PostForm

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class Postsearch(ListView):
    model = Post
    template_name = 'news/template/news/search.html'
    context_object_name = 'search'
    ordering = ['-dateCreation']
    paginate_by = 10
    # form_class = PostForm

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(PermissionRequiredMixin, DetailView):
    template_name = 'news/template/news/detail.html'
    queryset = Post.objects.all()
    permission_required = ('news.view_post',)


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'news/template/news/post_create.html'
    form_class = PostForm
    success_url = '/'
    permission_required = ('news.add_post',)




class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'news/template/news/post_create.html'
    form_class = PostForm
    success_url = '/'
    permission_required = ('news.change_post',)

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin,DeleteView):
    template_name = 'news/template/news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/'
    permission_required = ('news.delete_post',)
    # def get_object(self, **kwargs):
    #     id = self.kwargs.get('pk')
    #     return Post.objects.get(pk=id)