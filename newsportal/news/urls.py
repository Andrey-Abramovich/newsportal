from django.contrib import admin
from django.urls import path
from .views import  Posts, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    # path('', index, name = 'index'),
    # path('search/<int:pk>', detail, name = 'detail'),
    path('', Posts.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_create'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete')
]