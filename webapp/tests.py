

from django.test import TestCase
from django.test.client import Client
from webapp.models import Flight, House, User


class StaticPagesTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_homepage(self):
        r = self.c.get('/')
        self.assertIn(r.status_code, (200, 302))

    def test_my_flights(self):
        r = self.c.get('/My_Flights/')
        self.assertIn(r.status_code, (200, 302))

    def test_all_flights(self):
        r = self.c.get('/All_Flights/')
        self.assertIn(r.status_code, (200, 302))

    def test_houses(self):
        r = self.c.get('/Houses/')
        self.assertIn(r.status_code, (200, 302))

    def test_sdf_page(self):
        r = self.c.get('/sdf_page/')
        self.assertIn(r.status_code, (200, 302))

    def test_signup_page(self):
        r = self.c.get('/Signup_Page/')
        self.assertIn(r.status_code, (200, 302))

    def test_about_us(self):
        r = self.c.get('/About_Us/')
        self.assertIn(r.status_code, (200, 302))

    def test_people(self):
        r = self.c.get('/People/')
        self.assertIn(r.status_code, (200, 302))
