from django.contrib import admin
from .models import Profilen, News


class ProfilenAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'city']


admin.site.register(Profilen, ProfilenAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'header']


admin.site.register(News, NewsAdmin)
