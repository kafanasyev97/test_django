from rest_framework import serializers
from .models import Itemnew, Author, Book


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemnew
        fields = ['id', 'name', 'description', 'weight']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'last_name', 'year_birth']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'pages', 'auth', 'year']

