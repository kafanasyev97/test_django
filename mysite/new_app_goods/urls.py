from django.urls import path
from .views import ItemnewList, AuthorList, BookList, ItemDetail


urlpatterns = [
    path('items/', ItemnewList.as_view(), name='items_list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='items_detail'),
    path('authors/', AuthorList.as_view(), name='authors_list'),
    path('books/', BookList.as_view(), name='books_list'),
]
