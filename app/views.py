from django.shortcuts import render, redirect, get_object_or_404
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
        nutrition_grades = "e"

        # Search for different categories for the desired food
        for product in Product.objects.filter(name__icontains=query):
            for category in product.categories.all():
                if category.name not in cat_list:
                    cat_list.append(category.name)
                if product.nutrition_grades < nutrition_grades:
                    nutrition_grades = product.nutrition_grades

    # List of products of the first category found
    if len(cat_list) != 0:
        products = Product.objects.filter(categories__name=cat_list[0], name__icontains=query)
        results = [product for product in products if product.nutrition_grades <= nutrition_grades]
    else:
        results = None
    context = {
        'search': query,
        'products': results
    }
    return render(request, 'app/results.html', context)


def my_foods(request):
    pass


def food(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'app/food.html', context)


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
