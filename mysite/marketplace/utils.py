from .forms import OrdernewForm
from .models import Good


def reduce_user_balance(request):
    form = OrdernewForm(request.POST)
    if form.is_valid():
        products = form.cleaned_data['products']
        for x in products:
            a = x
            print(a)
            print(request.user.profilenew.balance)
            request.user.profilenew.balance -= a.price
            print(request.user)
            print(request.user.profilenew.balance)
        request.user.profilenew.save()


def reduce_count_good(request):
    form = OrdernewForm(request.POST)
    if form.is_valid():
        products = form.cleaned_data['products']
        for x in products:
            print(x.count)
            x.count -= 1
            print(x.count)
            print(request.POST)
            print(x)
            x.save()


