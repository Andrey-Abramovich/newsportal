from django.urls import path
from .views import Posts, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, Postsearch
# from .views import  IndexView

urlpatterns = [
    # path('', index, name = 'index'),
    # path('search/<int:pk>', detail, name = 'detail'),
    path('', Posts.as_view()),
    # path('', IndexView.as_view()),
    path('search/', Postsearch.as_view(), name='search'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_create'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete')
]