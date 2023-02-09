from django.urls import path
from .views import main, register_news, NewsLoginView, create_news



app_name = 'news_site'

urlpatterns = [
    path('', main, name='main'),
    path('register/', register_news, name='register'),
    path('login/', NewsLoginView.as_view(), name='login'),
    path('create_news/', create_news, name='create_news'),
    ]