from django.db import transaction
from django.shortcuts import render


@transaction.atomic
def publish_blog_post(post_id, user_id, scope_value):
    # функция уменьшения баланса пользователя на какое то значение(user_id, scope_value)
    # функция публикации поста(post_id)
    pass

