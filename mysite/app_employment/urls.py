from django.urls import path
from .views import vacancy_list


app_name = 'app_employment'

urlpatterns = [
    path('vacancy/', vacancy_list, name='vacancy_list'),
    ]

