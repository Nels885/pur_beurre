from django.db import models
from django.contrib.auth.models import User

from app.models import Product

# Create your models here.


class Backup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subs_product = models.ForeignKey(Product, related_name='%(class)s_substitute', on_delete=models.CASCADE,
                                     null=True)
    search_product = models.ForeignKey(Product, related_name='%(class)s_search', on_delete=models.CASCADE,
                                       null=True)
