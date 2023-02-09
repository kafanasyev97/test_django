from django.contrib.auth.models import User
from django.db import models


class Profilen(models.Model):  # Расширенная тадлица для пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(blank=False)
    city = models.CharField(max_length=36, blank=True)
    is_verified = models.BooleanField(default=False)


class News(models.Model):  # Создание новости
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    header = models.CharField(max_length=70, blank=False, null=False, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    tag = models.CharField(max_length=20, blank=True, null=False, verbose_name='Тег')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        permissions = (
            ('can_publish', 'Может публиковать'),
            ('can_verification', 'Может верифицировать'),
        )
