# Generated by Django 4.1.5 on 2023-02-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0002_alter_news_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='count_news',
            field=models.IntegerField(null=True),
        ),
    ]
