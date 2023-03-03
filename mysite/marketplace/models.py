from django.contrib.auth.models import User
from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=50)


class Good(models.Model):
    class Meta:
        ordering = ['count', 'name']
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    count = models.IntegerField(default=50)
    shops = models.ManyToManyField(Shop, related_name='goods')


class Profilenew(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, default=0, decimal_places=8)


class Ordernew(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Good, related_name='orders')


class History(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Promotion(models.Model):
    name = models.CharField(max_length=200)


class Offer(models.Model):
    name = models.CharField(max_length=200)



