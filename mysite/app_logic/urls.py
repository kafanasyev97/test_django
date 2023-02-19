from django.urls import path
from .views import welcome


app_name = 'app_logic'

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
]
