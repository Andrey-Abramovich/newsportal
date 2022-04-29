from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title', 'author', 'dateCreation', 'ratingpost') # генерируем список имён всех полей для более красивого отображения
    # list_filter = ('title', 'author', 'dateCreation') # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'title__title')  # тут всё очень похоже на фильтры из запросов в базу


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'ratingauthor')
    list_filter = ['authorUser']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    # search_fields = ('name', 'category__name')
    search_fields = ('name', 'postcategory__category_across__name')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(PostCategory)
# admin.site.register(Comment)

