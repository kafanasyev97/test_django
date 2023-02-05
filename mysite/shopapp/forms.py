from django import forms
from .models import Product, Order
from django.contrib.auth.models import Group


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'name', 'price', 'description', 'discount'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'delivery_address', 'promocode', 'user', 'products'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

