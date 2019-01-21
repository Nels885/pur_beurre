from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from app.models import Product
from .models import Backup

# Create your tests here.


# Test My Foods Page
class MyFoodsPageTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeattles.com', 'johnpassword')
        user.last_name = 'lennon'
        user.save()
        search = Product.objects.create(
            barcode="0123456789",
            name="Nutella",
            category="Pâte à tartiner",
            url="https://fr.openfoodfacts.org/produit/3017620406003/nutella-ferrero",
            front_picture="https://static.openfoodfacts.org/images/products/301/762/040/6003/front_fr.108.400.jpg",
        )
        subs = Product.objects.create(
            barcode="9876543210",
            name="Purée de Cacahuète",
            category="Pâte à tartiner",
            url="https://fr.openfoodfacts.org/produit/3390390000153/puree-de-cacahuete-jean-herve",
            front_picture="https://static.openfoodfacts.org/images/products/339/039/000/0153/front_fr.58.400.jpg")
        self.product = Product.objects.get(name="Nutella")
        self.backup = Backup.objects.create(user=user, subs_product=subs, search_product=search)

    def test_my_foods_page_redirect(self):
        response = self.client.get(reverse('save:my_foods'))
        self.assertEqual(response.status_code, 302)

    def test_my_foods_page_returns_200(self):
        self.client.login(username="john", password="johnpassword")
        response = self.client.get(reverse('save:my_foods'))
        self.assertEqual(response.status_code, 200)

    def test_food_is_delete(self):
        old_backup = Backup.objects.count()
        subs_id = self.backup.id
        self.client.login(username="john", password="johnpassword")
        response = self.client.get(reverse('save:delete', args=(subs_id,)))
        new_backup = Backup.objects.count()
        self.assertEqual(new_backup, old_backup - 1)
