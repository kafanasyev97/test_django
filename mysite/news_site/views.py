from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from .forms import RegisterFormNews, NewsForm
from .models import Profilen


def main(request):                 # Главная страница
    return render(request, 'news_site/main.html')


def register_news(request):    # Регистрация пользователя
    if request.method == 'POST':
        form = RegisterFormNews(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            city = form.cleaned_data.get('city')
            is_verified = form.cleaned_data.get('is_verified')
            Profilen.objects.create(
                user=user,
                phone_number=phone_number,
                city=city,
                is_verified=is_verified,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/news')
    else:
        form = RegisterFormNews()
        return render(request, 'news_site/register_news.html', {'form': form})


class NewsLoginView(LoginView):    # Аутентификация пользователя
    template_name = 'news_site/login_news.html'


def create_news(request: HttpRequest):   # Создание новости
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('news_site:main')
            return redirect(url)
    else:
        form = NewsForm()
        context = {
            'form': form,
        }
        return render(request, 'news_site/create_news.html', context=context)


class ProfilenDetailsView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        profile = Profilen.objects.get(pk=request.user.profilen.pk)
        context = {
            'profile': profile
        }
        return render(request, 'news_site/account.html', context=context)

