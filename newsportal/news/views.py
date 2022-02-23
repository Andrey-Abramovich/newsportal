from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post, Category
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .filters import PostFilter
from .forms import PostForm


# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html', context={'posts': posts})


# def detail(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'detail.html', context={'post': post})


class Posts(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']
    paginate_by = 10
    # form_class = PostForm

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    # def get_context_data(self, *args, **kwargs):
    #     return {
    #         **super().get_context_data(*args, **kwargs),
    #         'filter': self.get_filter(),
    #     }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())

        # context['categories'] = Category.objects.all()
        # context['form'] = PostForm()
        return context

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
    #
    #     if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
    #         form.save()
    #
    #     return super().get(request, *args, **kwargs)

        # title = request.POST['title']
        # postCategories_id = request.POST['categories']
        # content_post = request.POST['content_post']
        #
        # post = Post(title=title, postCategories_id=postCategories_id, content_post=content_post)  # создаём новый товар и сохраняем
        # post.save()
        # return super().get(request, *args, **kwargs)


class PostDetailView(DetailView):
    # model = Post
    template_name = 'detail.html'
    queryset = Post.objects.all()
    # success_url = '/<int:pk>/'

    # def get_object(self, **kwargs):
    #     id = self.kwargs.get('pk')
    #     return Post.objects.get(pk=id)


class PostCreateView(CreateView):
    # model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    # def get_object(self, **kwargs):
    #     id = self.kwargs.get('pk')
    #     return Post.objects.get(pk=id)


class PostUpdateView(UpdateView):
    # model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    # success_url = '/news/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    # model = Post
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

    # def get_object(self, **kwargs):
    #     id = self.kwargs.get('pk')
    #     return Post.objects.get(pk=id)