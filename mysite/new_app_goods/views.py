from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView
from .models import Itemnew, Author, Book
from .entities import Item
from rest_framework.response import Response
from .serializers import ItemSerializer, AuthorSerializer, BookSerializer
from rest_framework.generics import GenericAPIView


class ItemnewList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка товаров и создания нового товара."""
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Itemnew.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class AuthorList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка авторов и создания нового автора."""
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class BookList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка книг и создания новой книги."""
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        item_auth = self.request.query_params.get('auth')
        item_name = self.request.query_params.get('name')
        item_page = self.request.query_params.get('pages')
        if item_auth and item_name:
            queryset = queryset.filter(auth=item_auth, name=item_name)
        if item_page > '500':
            queryset = queryset.filter(pages=item_page)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class ItemDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о товаре, а также для его редактирования и удаления"""
    queryset = Itemnew.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)








# class ItemnewList(ListModelMixin, CreateModelMixin, GenericAPIView):      до фильтрации
#     queryset = Itemnew.objects.all()
#     serializer_class = ItemSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request, format=None):
#         return self.create(request)





# class ItemnewList(APIView):        первый вариант до 13.5
#     def get(self, request):
#         items = Itemnew.objects.all()
#         serializer = ItemSerializer(items, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)






# def items_list(request):    какая то хрень ненужная
#     if request.method == 'GET':
#         items_for_sale = [
#             Item(
#                 name='Кофеварка',
#                 description='Варит отличный кофе',
#                 weight=100
#             ),
#             Item(
#                 name='Беспроводные наушники',
#                 description='Отличный звук',
#                 weight=150
#             )
#         ]
#         return JsonResponse(ItemSerializer(items_for_sale, many=True).data, safe=False)
