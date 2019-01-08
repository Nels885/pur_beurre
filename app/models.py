from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    barcode = models.CharField(max_length=100, unique=True, null=True)
    name = models.CharField(max_length=200)
    nutrition_grades = models.CharField(max_length=10)
    nutrition_picture = models.URLField(null=True)
    url = models.URLField()
    front_picture = models.URLField(null=True)
    category = models.URLField(max_length=200)


class Backup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subs_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    search_product = models.IntegerField(null=True)
