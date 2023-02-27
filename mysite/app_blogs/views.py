from django.db import transaction
from django.shortcuts import render
from .models import Post
import logging


logger = logging.getLogger(__name__)


@transaction.atomic
def publish_blog_post(post_id, user_id, scope_value):
    # функция уменьшения баланса пользователя на какое то значение(user_id, scope_value)
    # функция публикации поста(post_id)
    pass


def posts_list(request):
    posts = Post.objects.select_related('blog').only('title', 'blog__name').order_by('blog').all()
    logger.info('Запрошена страница со списком записей блогов')
    return render(request, 'app_blogs/posts_list.html', {'post_list': posts})

