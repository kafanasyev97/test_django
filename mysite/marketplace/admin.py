from django.contrib import admin
from .models import Shop, Good


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
