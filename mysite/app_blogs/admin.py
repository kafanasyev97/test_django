from django.contrib import admin

from .models import Bloog, Post, Author


class BloogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Bloog, BloogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
