from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Product, Backup

from .forms import RegistrationForm


# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def search(request):
    query = request.GET.get('query')
    if not query:
        return redirect('/')
    else:
        category = None
        nutrition_grades = "e"

        # Search for different categories for the desired food
        for product in Product.objects.filter(name__icontains=query):
                if product.nutrition_grades < nutrition_grades:
                    nutrition_grades = product.nutrition_grades
                    category = product.category

    # List of products of the first category found
    if category:
        results = Product.objects.filter(category=category)
        # results = [product for product in products if product.nutrition_grades <= nutrition_grades]
    else:
        results = None
    context = {
        'search': query,
        'products': results
    }
    return render(request, 'app/results.html', context)


@login_required
def my_foods(request):
    pass


def food(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'app/food.html', context)


# @login_required(login_url='/app/login/')
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
