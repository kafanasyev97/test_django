from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ordernew


class RegisterForm(UserCreationForm):
    balance = forms.DecimalField(max_digits=10)

    class Meta:
        model = User
        fields = ('username', 'balance', 'password1', 'password2')


class UpdateBalanceForm(forms.Form):
    balance = forms.DecimalField(max_digits=10, decimal_places=8)


class OrdernewForm(forms.ModelForm):
    class Meta:
        model = Ordernew
        fields = 'products', 'user'
