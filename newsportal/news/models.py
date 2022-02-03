from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingauthor = models.IntegerField(default=0)

    def update_rating(self):
        upd_ratingpost = self.post_set.aggregate(Ratingpost = Sum('ratingpost'))
        upRat = 0
        upRat += upd_ratingpost.get('Ratingpost')

        upd_comment_rating = self.authorUser.comment_set.aggregate(Commentrating = Sum('comment_rating'))
        upCom = 0
        upCom += upd_comment_rating.get('Commentrating')

        self.ratingauthor = upd_ratingpost * 3 + upd_comment_rating
        self.save()


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
        self.ratingpost += 1
        self.save()

    def dizlike(self):
        self.ratingpost -= 1
        self.save()

    def Preview(self):
        return f'{self.content[0:100]} + "..."'


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
        self.comment_rating += 1
        self.save()

    def dizlike(self):
        self.comment_rating -= 1
        self.save()

