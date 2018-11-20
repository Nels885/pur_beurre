from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Product, Category

# Create your tests here.


# Test Index Page
class IndexPageTestCase(TestCase):

    # Test index page returns status code 200
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


# Test Account Page
class AccountPageTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeattles.com', 'johnpassword')
        user.last_name = 'lennon'
        user.save()
        self.user = User.objects.get(username='john')

    # Test if user is registered
    def test_user_is_registered(self):
        old_users = User.objects.count()
        response = self.client.post(reverse('app:account'), {
            'username': 'toto',
            'email': 'toto@mail.com',
            'password1': 'totopassword',
            'password2': 'totopassword'
        })
        new_users = User.objects.count()
        self.assertEqual(new_users, old_users + 1)

    # Test if user is not valid
    def test_user_is_not_valid(self):
        old_users = User.objects.count()
        username = self.user.username
        email = self.user.email
        password = self.user.password
        response = self.client.post(reverse('app:account'), {
            'username': username,
            'email': email,
            'password1': password,
            'password2': password
        })
        new_users = User.objects.count()
        self.assertEqual(new_users, old_users)


# Test Result Page
class ResultPageTestCase(TestCase):

    def setUp(self):
        nutella = Product.objects.create(name="Nutella")
        category = Category.objects.create(name="Chocolat")
        category.products.add(nutella)
        self.product = Product.objects.get(name="Nutella")

    def test_result_page(self):
        response = self.client.get(reverse('app:search'), {
            'query': 'nutella'
        })
        self.assertEqual(response.status_code, 200)
