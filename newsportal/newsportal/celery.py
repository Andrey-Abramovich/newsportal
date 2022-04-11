import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsportal.settings')
app = Celery('newsportal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send_mail_every_monday': {
        'task': 'news.tasks.send_week_mail',
        'schedule': crontab(day_of_week='mon', hour='8', minute='0'),
        # 'schedule': crontab(minute='*/5'),
    },
}
