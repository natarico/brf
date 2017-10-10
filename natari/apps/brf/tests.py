from django.test import TestCase, Client
from django.urls import resolve
from .views import sign_up
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_sign_up_page(self):
        found = resolve('/')
        self.assertEqual(found.func, sign_up)

    def test_home_page_returns_correct_html(self):
        response=self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>BRF</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'signup.html')
        self.assertIn('form', html)
    
class RegisterTest(TestCase):
    def test_register_can_register_with_POST(self):
        user = User.objects.create()
        second_user = User.objects.create()

        self.client.post('')