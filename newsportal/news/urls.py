from django.contrib import admin
from django.urls import path
from .views import detail, Posts


urlpatterns = [
    # path('', index, name = 'index'),
    path('search/<int:id>', detail, name = 'detail'),
    path('search', Posts.as_view())
]