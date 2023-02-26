from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Profileblog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True)


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    description = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Utro(models.Model):
    age = models.IntegerField(blank=True)


class MyBlog(models.Model):
    class Meta:
        ordering = ['-created_at']
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    description = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


