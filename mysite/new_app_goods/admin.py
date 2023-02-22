from django.contrib import admin
from .models import Itemnew, Author, Book


class ItemnewAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Itemnew, ItemnewAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name']


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Book, BookAdmin)
