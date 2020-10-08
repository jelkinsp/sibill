from django.test import TestCase
from rest_framework import status
import json
import requests


class InvoiceTest(TestCase):
    def setUp(self):
        pass

    def test_create(self):
        test_post = '{"user_id": 2, "products": [1, 2, 3, 4]}'

        url = "http://localhost:8000/sibill/invoice/"

        response = requests.request("POST", url, data=test_post)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", result)
        self.assertIn("date_invoice", result)
        self.assertIn("iva", result)
        self.assertIn("total", result)
        self.assertIn("products", result)

    def test_get_by_id(self):
        invoice_id = 41
        url = "http://localhost:8000/sibill/invoice/{}".format(invoice_id)

        response = requests.request("GET", url)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("id", result)
        self.assertIn("date_invoice", result)
        self.assertIn("iva", result)
        self.assertIn("total", result)
        self.assertIn("products", result)

    def test_get_by_user_product(self):
        user_name = "user1"
        year = 2020
        url = "http://localhost:8000/sibill/invoice/{}/{}".format(user_name, year)

        response = requests.request("GET", url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        url = "http://localhost:8000/sibill/invoice/"

        test_delete = '{"id":12}'

        response = requests.request("DELETE", url, data=test_delete)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_create_error(self):
        test_post = '{"user_id": 100, "products": [1, 2, 3, 4]}'

        url = "http://localhost:8000/sibill/invoice/"

        response = requests.request("POST", url, data=test_post)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_by_id_error(self):
        invoice_id = 200
        url = "http://localhost:8000/sibill/invoice/{}".format(invoice_id)

        response = requests.request("GET", url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_by_user_product_error(self):
        user_name = "user3"
        year = 2020
        url = "http://localhost:8000/sibill/invoice/{}/{}".format(user_name, year)

        response = requests.request("GET", url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_error(self):
        url = "http://localhost:8000/sibill/invoice/"

        test_delete = '{"id":12}'

        response = requests.request("DELETE", url, data=test_delete)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
