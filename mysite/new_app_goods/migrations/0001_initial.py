# Generated by Django 4.1.5 on 2023-02-21 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itemnew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('weight', models.FloatField(verbose_name='вес')),
            ],
        ),
    ]