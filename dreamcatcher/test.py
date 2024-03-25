from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Dream


class TestDreamsModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_admin', password='test_pass')
        self.data1 = Dream.objects.create(user=self.user.username, descriere='Vis urat', eticheta='Cosmar', stres=5,
                                          nivelEnergie=1, durata=4)

    def test_dreams_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Dream))

    def test_dreams_model_user(self):
        dream = Dream.objects.get(id=1)
        self.assertEqual(dream.user, 'test_admin')

    def test_dreams_model_filter(self):
        Dream.objects.create(user='test_admin', descriere='Vis frumos', eticheta='Vise recurente', stres=1,
                             nivelEnergie=5,
                             durata=3)
        dreams = Dream.objects.filter(user='test_admin', stres__lte=3)
        self.assertEqual(len(dreams), 1)
        self.assertEqual(dreams[0].descriere, 'Vis frumos')

    def test_dreams_model_delete(self):
        Dream.objects.get(id=1).delete()
        self.assertEqual(Dream.objects.count(), 0)


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_admin', password='test_pass')
        self.dream = Dream.objects.create(user=self.user.username, descriere='Vis urat', eticheta='Cosmar', stres=5,
                                          nivelEnergie=1, durata=4)

    def test_login_page(self):
        response = self.client.get(reverse('dreamcatcher:login_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_success(self):
        response = self.client.post(reverse('dreamcatcher:login_view'),
                                    {'username': 'test_admin', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'descriere_categorie.html')

    def test_login_view_failure(self):
        response = self.client.post(reverse('dreamcatcher:login_view'),
                                    {'username': 'invalid_user', 'password': 'invalid_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_register(self):
        response = self.client.post(reverse('dreamcatcher:login_register'),
                                    {'username': 'new_user', 'password': 'new_pass', 'firstname': 'New',
                                     'lastname': 'User'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_register.html')

    def test_descriere_categorie(self):
        self.client.login(username='test_admin', password='test_pass')
        response = self.client.get(reverse('dreamcatcher:descriere_categorie'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'descriere_categorie.html')

    def test_rating(self):
        self.client.login(username='test_admin', password='test_pass')
        response = self.client.post(reverse('dreamcatcher:rating'),
                                    {'description': 'Vis ingrozitor', 'category': 'Cosmar'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rating.html')
        dream = Dream.objects.get(id=self.dream.id + 1)
        self.assertEqual(dream.user, self.user.username)
        self.assertEqual(dream.descriere, 'Vis ingrozitor')
        self.assertEqual(dream.eticheta, 'Cosmar')

