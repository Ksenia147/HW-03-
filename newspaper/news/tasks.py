from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from news.management.commands.runapscheduler import my_job
from news.models import Post, Category
from django.conf import settings



@shared_task
def celery_notify_new_post(pk):
    instance = Post.objects.get(pk=pk)
    categories = instance.categories.all()

    subscribers_emails = []
    for category in categories:
        subscribers = category.subscribers.all()
        subscribers_emails += [s.email for s in subscribers]

    preview = instance.preview()

    html_content = render_to_string(
        'new_post_email.html',
        {
            'title': instance.title,
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject='Новая статья уже на сайте',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def celery_weekly_mailing():
    today = datetime.now()
    last_week = today - timedelta(days=7)
    posts = Post.objects.filter(created_at__gte=last_week)
    categories = set(posts.values_list('categories__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_news.html',
        {
            'link': settings.SITE_URL,
            'posts': posts
        }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()