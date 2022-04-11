from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, Category
from django.utils import timezone

# from django.contrib.sites.shortcuts import get_current_site


@shared_task
def send_week_mail(url=None):
    for category in Category.objects.all():
        subscribers = category.subscribers.all()
        posts = Post.objects.filter(postcategory__category_across=category,
                                    dateCreation__range=[timezone.now() - timezone.timedelta(days=7), timezone.now()])
        # full_url = ''.join(['http://', get_current_site(None).domain, ':8000'])

        # print('sub', category, subscribers)
        # print('week', week_news)
        # print('posts', posts)
        # print('url', full_url)
        for subscriber in subscribers:
            recipient_list = []
            recipient_list.append(subscriber.email),
            # print('list', recipient_list)

            content = render_to_string('news/weeknews.html', {'posts': posts, 'category': category})
            msg = EmailMultiAlternatives(
                subject=f'Новости за неделю',
                from_email='andrey-abtest@yandex.ru',
                to=recipient_list,
            )
            msg.attach_alternative(content, "text/html")
            msg.send()
            print('weeknews отправил')

