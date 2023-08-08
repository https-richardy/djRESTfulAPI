from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class SimpleAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def getEndpoint(self, endpoint: str):
        return reverse(endpoint)
