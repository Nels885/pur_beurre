from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Product

from .forms import RegistrationForm


# Create your views here.


def index(request):
    """
    View of the index page
    :param request:
        Parameters of the request
    :return:
        Index page
    """
    return render(request, 'app/index.html')


def search(request):
    """
    View of the food search
    :param request:
        Parameters of the request
    :return:
        Results page or Index page if no found
    """
    query = request.GET.get('query')
    if not query:
        return redirect('/')
    else:

        # Search food in the database
        products = Product.objects.filter(name__icontains=query).order_by('-nutrition_grades')

        # Search for alternative foods
        if products:
            product = products[0]
            substitutes = Product.objects.filter(category=product.category,
                                                 nutrition_grades__lt=product.nutrition_grades).order_by(
                'nutrition_grades')
        else:
            product = substitutes = None

    context = {
        'search': query,
        'product': product,
        'substitutes': substitutes
    }
    return render(request, 'app/results.html', context)


def food(request, product_id):
    """
    View of the food in detail
    :param request:
        Parameters of the request
    :param product_id:
        Id of the food
    :return:
        Food page with the detail
    """
    product = get_object_or_404(Product, pk=product_id)
    picture_header = product.front_picture.replace("400.jpg", "full.jpg")
    context = {
        'picture_header': picture_header,
        'product': product
    }
    return render(request, 'app/food.html', context)


@login_required(login_url='/app/login/')
def account(request):
    """
    view of logged user information
    :param request:
        Parameters of the request
    :return:
        Account page with user information
    """
    return render(request, 'app/account.html')


def registration(request):
    """
    View for registration of a new user
    :param request:
        Parameters of the request
    :return:
        Registration page or login page
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/login/')
        context = {'form': form}
    else:
        form = RegistrationForm()
        context = {'form': form}
    return render(request, 'app/registration.html', context)
