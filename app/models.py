from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    nutrition_grades = models.CharField(max_length=10)
    nutrition_picture = models.URLField()
    url = models.URLField()
    front_picture = models.URLField()
    category = models.URLField(max_length=200)


class Backup(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
