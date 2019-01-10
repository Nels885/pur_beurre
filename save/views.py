from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from app.models import Product, Backup

# Create your views here.


@login_required(login_url='/app/login/')
def my_foods(request):
    """
    View of different foods backed up according to the user
    :param request:
        Parameters of the request
    :return:
        My_foods page
    """
    user = request.user
    backups = Product.objects.filter(backup__user=user.id)

    if len(backups) == 0:
        backups = None

    context = {
        'substitutes': backups
    }

    return render(request, 'save/my_foods.html', context)


@login_required(login_url='/app/login/')
def backup(request, search_prod, subs_id):
    """
    View of the food saved by the user
    :param request:
        Parameters of the request
    :param search_prod:
        Name of the search product
    :param subs_id:
        Id of substitute product
    :return:
        My_foods page
    """
    user = User.objects.get(pk=request.user.id)
    subs_product = Product(pk=subs_id)
    search_prod = Product(name=search_prod)
    Backup.objects.create(user=user, subs_product=subs_product, search_product=search_prod)

    return redirect('/save/my_foods')
