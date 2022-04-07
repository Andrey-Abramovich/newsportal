from datetime import timedelta, datetime
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import Post, Category, PostCategory
from django.utils import timezone


def send_week_mail(url=None):
    for category in Category.objects.all():
        subscribers = category.subscribers.all()
        # week_news = Post.objects.filter(dateCreation__range = [timezone.now() - timezone.timedelta(days=7),timezone.now()])
        posts = Post.objects.filter(postcategory__category_across=category,
                                    dateCreation__range=[timezone.now() - timezone.timedelta(days=7), timezone.now()])
        print('sub', category, subscribers)
        # print('week', week_news)
        print('posts', posts)
        for subscriber in subscribers:
            recipient_list = []
            recipient_list.append(subscriber.email),
            print('list', recipient_list)

            content = render_to_string('news/weeknews.html', {'posts': posts, 'category': category})
            msg = EmailMultiAlternatives(
                subject=f'Новости за неделю',
                from_email='andrey-abtest@yandex.ru',
                to=recipient_list,
            )
            msg.attach_alternative(content, "text/html")
            msg.send()
            print('weeknews отправил')



#
# def send_week_mail():
#     categories = Category.objects.all()
#     print('1-', categories)
#
#     for category in categories:
#         subscribers = Category.objects.filter(subscription__name=id)
#         print('2-', subscribers)
#         subscribers_emails = []
#         for user in subscribers:
#             subscribers_emails.append(user.email)
#
#             posts = Post.objects.filter(postcategory__category_across=id)
#
#             content = render_to_string('news/weeknews.html',
#                                        {'posts': posts,
#                                         'category': category
#                                         }
#                                        )

    # category_week = Category.objects.all()
    # print('1-', category_week)
    # # week_post = Post.objects.all().exclude(title__range=[datetime.now() - timedelta(days=7), datetime.now()])
    # week_post = Post.objects.filter(dateCreation__range = [datetime.now() - timedelta(days=7), datetime.now()])
    # # print('week_post', week_post)
    #
    # subscribers_emails = []
    #
    # for category in category_week:
    #     subscribers = User.objects.filter(subscription__name=id)
    #     # print('subscr', category.subscribers)
    #     print('2-', category)
    #
    #
    #     for user in subscribers:
    #         subscribers_emails.append(user.email)
    #         print('3-', subscribers_emails)
    #         posts = Post.objects.filter(postcategory__category=id)
    #         content = render_to_string('news/weeknews.html',
    #                                    {'posts': posts,
    #                                     'category': category
    #                                     }
    #                                    )



    # for category in Category.objects.all():
    #     subscribers = category.subscribers.all()
    #     # print('sub-', subscribers)
    #     week_news = Post.objects.filter(dateCreation__range = [timezone.now() - timedelta(days=7), timezone.now()])
    #     # print('wn-', week_news)
    #
    #     for subscriber in subscribers:
    #         for week_new in week_news:
    #             recipient_list = [subscriber.email]
    #             # subscribers_emails.append(user.email)
    #             # print('3-', subscribers_emails)
    #             posts = Post.objects.filter(postcategory__category_across= id)
    #             content = render_to_string('news/weeknews.html', {'posts': posts, 'category': category})

                # msg = EmailMultiAlternatives(
                #     subject=f'Новости за неделю',
                #     from_email='settings.DEFAULT_FROM_EMAIL',
                #     to=recipient_list,
                # )
                # msg.attach_alternative(content, "text/html")
                # msg.send()
                # print('weeknews отправил')
