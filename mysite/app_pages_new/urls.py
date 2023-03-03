from django.urls import path
from django.views.decorators.cache import cache_page
from .views import welcome, main_page


urlpatterns = [
    path('welcome/', cache_page(30)(welcome), name='welcome'),
    path('main_page/', main_page, name='main_page'),
]
