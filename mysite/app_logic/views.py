from django.shortcuts import render


def welcome(request):
    return render(request, 'app_logic/welcome.html')
