from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client

from app.models import Product, Backup

# Create your tests here.


# Test My Foods Page
class MyFoodsPageTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        user = User.objects.create_user('john', 'lennon@thebeattles.com', 'johnpassword')
        user.last_name = 'lennon'
        user.save()
        self.user = User.objects.get(username='john')
        search = Product.objects.create(name="Nutella", category="Pâte à tartiner")
        subs = Product.objects.create(name="Alter Eco", category="Pâte à tartiner")
        self.product = Product.objects.get(name="Nutella")
        Backup.objects.create(user_id=user.id, subs_product_id=subs.id, search_product=search.id)

    def test_my_foods_is_not_login_page(self):
        response = self.client.get(reverse('save:my_foods'))
        self.assertEqual(response.status_code, 302)

    def test_my_foods_page(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('save:my_foods'))
        self.assertEqual(response.status_code, 200)
        pass
