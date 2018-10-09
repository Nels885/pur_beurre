from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def results(request):
    pass


def my_foods(request):
    pass


def food(request):
    pass


def account(request):
    return render(request, 'app/account.html')


def logout(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'app/index.html')

