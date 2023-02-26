from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView
from .utils import reduce_count_good, reduce_user_balance
from .forms import RegisterForm, UpdateBalanceForm, OrdernewForm
from .models import Profilenew, Good, Shop, Ordernew


def another_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            balance = form.cleaned_data.get('balance')
            Profilenew.objects.create(
                user=user,
                balance=balance,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/market/account')
    else:
        form = RegisterForm()
    return render(request, 'marketplace/register.html', {'form': form})


class AccountView(View):
    def get(self, request):
        return render(request, 'marketplace/account.html')


class AnotherLoginView(LoginView):
    template_name = 'marketplace/login.html'


def update_balance_get(request, pk):   # обновляем баланс
    if request.method == 'POST':
        form = UpdateBalanceForm(request.POST)
        if form.is_valid():
            print(form)
            print(request.user.profilenew.balance)
            request.user.profilenew.balance += form.cleaned_data['balance']
            print(request.user.profilenew.balance)
            user = request.user.profilenew
            user.save()
            return redirect('marketplace:account')
    else:
        form = UpdateBalanceForm()
        return render(request, 'marketplace/update_balance.html', {'form': form})


class GoodListView(ListView):
    template_name = 'marketplace/goods_list.html'
    model = Good
    context_object_name = 'goods'


def create_order(request: HttpRequest):
    if request.method == 'POST':
        form = OrdernewForm(request.POST)
        if form.is_valid():
            result_order(request)
            form.save()
            url = reverse('marketplace:account')
            return redirect(url)
    else:
        form = OrdernewForm()
    context = {
        'form': form,
    }
    return render(request, 'marketplace/create_order.html', context=context)


@transaction.atomic
def result_order(request):
    reduce_user_balance(request)
    reduce_count_good(request)






