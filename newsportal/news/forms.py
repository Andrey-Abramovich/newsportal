from django.forms import ModelForm, CharField
from .models import Post, Category
from django import forms


# Создаём модельную форму
class PostForm(ModelForm):
    # title = forms.CharField()
    # author = Post.author
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'postCategory']