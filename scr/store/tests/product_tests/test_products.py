from store.tests import SimpleAPITestCase
from rest_framework import status

from store.models import (Product, Category)
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductAPITestCase(SimpleAPITestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Eletronics")
        product_image = SimpleUploadedFile(
            name='product_1.jpg',
            content=b'',
            content_type='image/jpeg'
        )
        Product.objects.create(
            title="Product 1",
            cover=product_image,
            description="Product description",
            category=self.category,
            price=200.00,
            stock=5
        )

    def test_list_products(self):
        response = self.client.get(self.getEndpoint('store:products-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
