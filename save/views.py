from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from app.models import Product
from save.models import Backup

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
    backups = Backup.objects.filter(user=user)

    if len(backups) == 0:
        backups = None

    context = {
        'substitutes': backups
    }

    return render(request, 'save/my_foods.html', context)


@login_required(login_url='/app/login/')
def backup(request, search_id, subs_id):
    """
    View of the food saved by user
    :param request:
        Parameters of the request
    :param search_id:
        Id of the search product
    :param subs_id:
        Id of substitute product
    :return:
        My_foods page
    """
    user = User.objects.get(pk=request.user.id)
    subs_product = Product(pk=subs_id)
    search_product = Product(pk=search_id)
    Backup.objects.create(user=user, subs_product=subs_product, search_product=search_product)

    return redirect('/save/my_foods')


@login_required(login_url='/app/login/')
def delete(request, subs_id):
    """
    View of the food deleted by user
    :param request:
        Parameters of the request
    :param subs_id:
        Id of substitute product
    :return:
        My_foods page
    """
    user = User.objects.get(pk=request.user.id)
    Backup.objects.get(user=user, pk=subs_id).delete()
    return redirect('/save/my_foods')
