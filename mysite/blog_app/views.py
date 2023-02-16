from _csv import reader

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView, ListView, DetailView
from .models import Profileblog, MyBlog
from .forms import RegisterForm, BlogForm, CsvForm


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            description = form.cleaned_data.get('description')
            Profileblog.objects.create(user=user, description=description)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/blog/account')
    else:
        form = RegisterForm()
    return render(request, 'blog_app/register.html', {'form': form})


class AnotherLoginView(LoginView):
    template_name = 'app_users/login.html'


class AnotherLogoutView(LogoutView):
    next_page = '/account'


class AccountView(View):
    def get(self, request):
        return render(request, 'blog_app/account.html')


class UserUpdateView(UpdateView):
    model = User
    form_class = RegisterForm
    template_name = 'blog_app/update_account.html'

    def get_success_url(self):
        return reverse(
            'blog_app:account',
        )


def upload_files(request: HttpRequest, pk):
    if request.method == 'POST' and request.user.is_authenticated:
        print(request.POST)
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = MyBlog(file=f, user_id=request.user.pk, description=request.POST['description'])
                instance.save()
            return redirect('/blog/account')
    else:
        form = BlogForm()
    return render(request, 'blog_app/create_post.html', {'form': form})


class BlogListView(ListView):
    template_name = 'blog_app/blogs-list.html'
    model = MyBlog
    context_object_name = 'blogs'


class BlogDetailsView(DetailView):
    template_name = 'blog_app/blogs-details.html'
    model = MyBlog
    context_object_name = 'blog'


def create_file_blog(request: HttpRequest):
    if request.method == 'POST':
        upload_file_form = CsvForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split()
            csv_reader = reader(price_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                MyBlog.objects.create(description=row[0], created_at=row[1])
            return HttpResponse(content='Запись была создана успешно', status=200)
    else:
        upload_file_form = CsvForm()
        context = {
            'form': upload_file_form
        }
        return render(request, 'blog_app/upload_file.html', context=context)

