from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import RegistrationFrom

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
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/login/')
        context = {'form': form}
    else:
        form = RegistrationFrom()
        context = {'form': form}
    return render(request, 'app/account.html', context)

