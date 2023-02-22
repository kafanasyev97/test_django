from django.urls import path
from .views import ItemnewList, AuthorList, BookList


urlpatterns = [
    path('items/', ItemnewList.as_view(), name='items_list'),
    path('authors/', AuthorList.as_view(), name='authors_list'),
    path('books/', BookList.as_view(), name='books_list'),
]
