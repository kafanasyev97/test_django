from django.db import models


class Itemnew(models.Model):
    """Модель товара."""
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    weight = models.FloatField(verbose_name='вес')


class Author(models.Model):
    """Модель автора."""
    name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')
    year_birth = models.IntegerField(verbose_name='год рождения')


class Book(models.Model):
    """Модель книги."""
    name = models.CharField(max_length=100, verbose_name='название')
    isbn = models.IntegerField(verbose_name='международный номер')
    year = models.IntegerField(verbose_name='год выпуска')
    pages = models.IntegerField(verbose_name='количество страниц')
    auth = models.ForeignKey(Author, on_delete=models.PROTECT)



