import json

from django.test import TestCase
from django.urls import reverse
from django_generic_contact.models import Contact
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,
)


class TestApi(TestCase):
    def setUp(self):
        super().setUp()
        self.contact = Contact.objects.create(
            name="Mr. Tester",
            message="Please contact me via email or phone.",
            data={
                "email": "mr@tester.com",
                "phone": "123456",
            },
        )

    def test_add_contact(self):
        data = {
            "name": "Mr. Tester",
            "message": "Please contact me via email or phone.",
            "data": json.dumps(
                {
                    "email": "mr@tester.com",
                    "phone": "123456",
                }
            ),
        }

        url = reverse("contact-list")
        response = self.client.post(url, data=data, format="json")
        self.assertEqual(HTTP_201_CREATED, response.status_code, response.content)

    def test_http_get_list_method_not_allowed(self):
        url = reverse("contact-list")
        response = self.client.get(url)
        self.assertEqual(
            HTTP_405_METHOD_NOT_ALLOWED, response.status_code, response.content
        )

    def test_http_get_single_contact_method_not_found(self):
        url = f"/api/contact/{self.contact.pk}/"
        response = self.client.get(url)
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code, response.content)

    def test_http_put_method_not_found(self):
        data = {
            "name": "Updated Tester",
            "message": "Updated message",
            "data": json.dumps(
                {
                    "email": "updated@tester.com",
                    "phone": "987654",
                }
            ),
        }

        url = f"/api/contact/{self.contact.pk}/"
        response = self.client.put(url, data=data, format="json")
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code, response.content)

    def test_http_patch_method_not_found(self):
        data = {
            "message": "Updated message",
        }

        url = f"/api/contact/{self.contact.pk}/"
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(HTTP_404_NOT_FOUND, response.status_code, response.content)
