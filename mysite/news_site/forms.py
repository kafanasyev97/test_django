from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import News


class RegisterFormNews(UserCreationForm):  # Форма для регистрации пользователя
    phone_number = forms.IntegerField(required=True)
    city = forms.CharField(required=False)
    is_verified = forms.BooleanField(required=False, disabled=True, initial=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class NewsForm(forms.ModelForm):  # Форма для создания новости
    class Meta:
        model = News
        fields = 'header', 'description', 'tag'
