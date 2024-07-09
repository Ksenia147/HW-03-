import datetime

from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import PostCategory, Post
from django.conf import settings
from .tasks import celery_notify_new_post

# def send_notifications(preview, pk, title, subscribers):
    # html_content = render_to_string(
    #     'new_post_email.html',
    #     {
    #         'title': title,
    #         'text': preview,
    #         'link': f'{settings.SITE_URL}/news/{pk}'
    #     }
    # )
    #
    # msg = EmailMultiAlternatives(
    #     subject='Новая статья уже на сайте',
    #     body='',
    #     from_email=settings.DEFAULT_FROM_EMAIL,
    #     to=subscribers,
    # )
    #
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()

# @receiver(m2m_changed, sender=PostCategory)
# def weekly_notify(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#
#         categories = instance.categories.all()
#         subscribers_emails = []
#         for category in categories:
#             subscribers = category.subscribers.all()
#             subscribers_emails += [s.email for s in subscribers]
#
#         send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)