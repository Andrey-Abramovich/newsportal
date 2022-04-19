from .models import *
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .signals import notify_post
from django.core.cache import cache


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

    template_name = 'news/index.html'
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
    template_name = 'news/search.html'
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
    template_name = 'news/detail.html'
    queryset = Post.objects.all()
    permission_required = ('news.view_post',)

    def get_object(self, *args, **kwargs):  # переопределяем метод получения объекта, как ни странно

        obj = cache.get(f'post-{self.kwargs["pk"]}',
                        None)  # кэш очень похож на словарь, и метод get действует так же. Он забирает значение по ключу, если его нет, то забирает None.

        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)

        return obj


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'news/post_create.html'
    form_class = PostForm
    success_url = '/'
    permission_required = ('news.add_post',)


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'news/post_create.html'
    form_class = PostForm
    success_url = '/'
    permission_required = ('news.change_post',)

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(PermissionRequiredMixin,DeleteView):
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/'
    permission_required = ('news.delete_post',)
    # def get_object(self, **kwargs):
    #     id = self.kwargs.get('pk')
    #     return Post.objects.get(pk=id)


class CategoryView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'news/categories.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'news/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        us = self.request.user
        id = self.kwargs.get('pk')
        sub_user = Category.objects.filter(id=id).values("subscribers__username")
        context['is_not_subscribe'] = not sub_user.filter(subscribers__username=self.request.user).exists()
        context['is_subscribe'] = sub_user.filter(subscribers__username=self.request.user).exists()
        # print('user-', sub_user)
        # print('context', context)
        # print("us=", us)
        # print('con+', context['is_not_subscribe'])

        return context


@login_required
def subscribe_me(request, pk):
    sub_user = User.objects.get(id=request.user.pk)
    # print(('us', sub_user))
    category_object = Category.objects.get(pk=pk)
    # print('cat', category_object)
    category_object.subscribers.add(sub_user)

    return redirect('/news/')


@login_required
def del_subscribe_me(request, pk):
    sub_user = User.objects.get(id=request.user.pk)
    print(('us', sub_user))
    category_object = Category.objects.get(pk=pk)
    print('cat', category_object)
    category_object.subscribers.remove(sub_user)

    return redirect('/news/')