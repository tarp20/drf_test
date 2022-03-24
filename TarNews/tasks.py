from celery import shared_task

from news.models import Post


@shared_task
def clean_upvotes():
    for post in Post.objects.all():
        post.upvotes = 0
        post.save()
    return "Upvotes have cleaned!"
