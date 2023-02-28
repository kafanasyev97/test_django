from django.urls import path
from .feeds import LatestNewsFeed


app_name = 'app_rss'

urlpatterns = [
    path('latest/feed/', LatestNewsFeed()),
]
