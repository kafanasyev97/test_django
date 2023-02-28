from django.contrib import admin
from .models import NewsItem, NewsType, HouseType, Room, House


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']


class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'count']


class HouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(NewsType, NewsTypeAdmin)
admin.site.register(HouseType, HouseTypeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(House, HouseAdmin)


