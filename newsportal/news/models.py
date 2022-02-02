from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete= models.CASCADE)
    ratingauthor = models.IntegerField(default=0)

    def rating_author(self):
        pass


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLES = 'AR'
    CATEGORIES = (
        (NEWS, 'Новости'),
        (ARTICLES, 'Статья')
    )
    category_choices = models.CharField(max_length=2, choices=CATEGORIES, default=NEWS)
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    content = models.TextField
    ratingpost = models.IntegerField(default=0)

    def like(self):
        pass

    def dizlike(self):
        pass


class PostCategory(models.Model):
    post_across = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_across = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_User = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        pass

    def dizlike(self):
        pass