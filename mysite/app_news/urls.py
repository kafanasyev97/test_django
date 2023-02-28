from django.urls import path
from .views import get_news_in_custom_format, NewsItemDetailView, HouseListView, ContactsListView, OurListView


app_name = 'app_news'

urlpatterns = [
    path('', get_news_in_custom_format, name='news_list'),
    path('<int:pk>/', NewsItemDetailView.as_view(), name='news-item'),
    path('houses/', HouseListView.as_view(), name='houses_list'),
    path('contacts/', ContactsListView, name='contacts_list'),
    path('our/', OurListView, name='our_list'),
]
