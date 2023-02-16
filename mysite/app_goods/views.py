from _csv import reader
from _decimal import Decimal

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Item
from .forms import UploadPriceForm


def items_list(request: HttpRequest):
    items = Item.objects.all()
    return render(request, 'app_goods/items_list.html', {'items_list': items})


def update_prices(request: HttpRequest):
    if request.method == 'POST':
        upload_file_form = UploadPriceForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split()
            csv_reader = reader(price_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
            return HttpResponse(content='Цены были успешно обновлены', status=200)
    else:
        upload_file_form = UploadPriceForm()
        context = {
            'form': upload_file_form
        }
        return render(request, 'app_media/upload_file.html', context=context)

