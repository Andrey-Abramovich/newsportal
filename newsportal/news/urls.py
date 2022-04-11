from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(Posts.as_view())),
    path('search/', Postsearch.as_view(), name='search'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_create'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('categories/subscribe/<int:pk>/', subscribe_me, name='subscribe'),
    path('categories/delsubscribe/<int:pk>/', del_subscribe_me, name='del_subscribe'),
]