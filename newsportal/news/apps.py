from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        import news.signals

        from .tasks import send_week_mail
        from .scheduler import news_sheduler
        print('started')

        news_sheduler.add_job(
            id='send_week_mail',
            func=send_week_mail,
            trigger='interval',
            seconds=5,
        )

        news_sheduler.start()

