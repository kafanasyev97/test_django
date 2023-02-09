from django.urls import path
from .views import login_view, AnotherLoginView, MainView, logout_view, AnotherLogoutView, register_view, \
    another_register_view

app_name = 'app_users'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('another_logout/', AnotherLogoutView.as_view(), name='another_logout'),
    path('register/', register_view, name='register'),
    path('another_register/', another_register_view, name='register'),
    ]

