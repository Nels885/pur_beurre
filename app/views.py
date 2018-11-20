from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import Product, Category, Backup

from .forms import RegistrationForm

# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def search(request):
    query = request.GET.get('query')
    if not query:
        return redirect('/')
    else:
        cat_list = []

        # Search for different categories for the desired food
        for product in Product.objects.filter(name__icontains=query):
            for category in product.categories.all():
                if category.name not in cat_list:
                    cat_list.append(category.name)

    # List of products of the first category found
    products = Product.objects.filter(categories__name=cat_list[0], name__icontains=query)
    context = {
        'search': query,
        'products': products
    }

    return render(request, 'app/results.html', context)


def my_foods(request):
    pass


def food(request):
    pass


def account(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/login/')
        context = {'form': form}
    else:
        form = RegistrationForm()
        context = {'form': form}
    return render(request, 'app/account.html', context)
