from django.urls import path
from .views import posts_list


app_name = 'app_blogs'

urlpatterns = [
    path('', posts_list, name='posts_list'),
    ]