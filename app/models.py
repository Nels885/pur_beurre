from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    nutrition_grades = models.CharField(max_length=10)
    url = models.URLField()
    picture = models.URLField()


class Category(models.Model):
    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, related_name='categories', blank=True)


class Backup(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
