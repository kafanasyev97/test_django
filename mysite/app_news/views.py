from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.core import serializers
from django.views import View
from django.views.generic import DetailView, ListView

from .models import NewsItem, House


def get_news_in_custom_format(request):
    format = request.GET['format']
    if format not in ['xml', 'json', 'yaml']:
        return HttpResponseBadRequest()
    data = serializers.serialize(format, NewsItem.objects.all())
    return HttpResponse(data)


class NewsItemDetailView(DetailView):
    model = NewsItem
    template_name = 'app_news/newsitem_detail.html'


class HouseListView(ListView):
    template_name = 'app_news/house_list.html'
    model = House
    context_object_name = 'products'


def ContactsListView(request):
    return render(request, 'app_news/contacts.html')


def OurListView(request):
    return render(request, 'app_news/our.html')

