# Generated by Django 4.1.5 on 2023-02-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
