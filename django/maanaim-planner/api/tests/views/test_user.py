from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import UserRegistration


class UserRegistrationViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {"username": "johndoe",
                          "email": "johndoe@example.com", "password": "securepassword"}
        self.user = UserRegistration.objects.create(**self.user_data)

    def test_get_users(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
