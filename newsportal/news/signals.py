from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *
from django.contrib.auth.models import User

@receiver(m2m_changed, sender=Post.postCategory.through)
def notify_post(sender, instance, **kwargs):
    changed_category = Category.objects.filter(postcategory__post_across=instance)
    if changed_category.count() == 1:
        # Достаем через гет измененную категорию
        category = Category.objects.get(postcategory__post_across=instance)
        # Собираем всех пользователей, подписанных на данную категорию
        subscribers = User.objects.filter(subscription__name=category)
        # Создаем списаок емейл адресов из пользователей
        email_subscribers = []
        for email in subscribers:
            email_subscribers.append(email.email)

        # Создаем html для передачи рассылки
        category = f'{instance.postCategory}'
        text = f'{instance.content}'
        theme = f'{instance.title}'
        # Достаем ид добавленной новости, для формирования ссылки
        url = f'{Post.objects.get(postcategory__post_across=instance).id}'

        msg = EmailMultiAlternatives(
            subject='Появились обновления в категории на которую вы подписаны',
            from_email='andrey-abtest@yandex.ru',
            to=email_subscribers,
        )
        content = render_to_string('news/addpost_email.html', {
            'category': category,
            'theme': theme,
            'text': text,
            'url': url,
        }
                                   )
        msg.attach_alternative(content, "text/html")  # добавляем html
        msg.send()  # отсылаем
