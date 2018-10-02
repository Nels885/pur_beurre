from django.test import TestCase
from django.urls import reverse

# Create your tests here.


# Test Index Page
class IndexPageTestCase(TestCase):

    # Test index page returns status code 200
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
