# Generated by Django 4.1.5 on 2023-02-21 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app_goods', '0002_author_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='year_birth',
            field=models.IntegerField(verbose_name='год рождения'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(verbose_name='международный номер'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(verbose_name='количество страниц'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(verbose_name='год выпуска'),
        ),
    ]