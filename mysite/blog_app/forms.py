import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyBlog


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    description = forms.CharField(max_length=100, required=False, help_text='О себе')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'description')


class BlogForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = MyBlog
        fields = 'description', 'file_field',


class CsvForm(forms.Form):
    file = forms.FileField()

