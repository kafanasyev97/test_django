from django.shortcuts import render
from django.views.decorators.cache import cache_page
from time import sleep


# @cache_page(30)
def welcome(request, *args, **kwargs):
    # sleep(4)
    return render(request, 'app_pages_new/welcome.html')


def main_page(request, *args, **kwargs):
    return render(request, 'app_pages_new/main.html')
