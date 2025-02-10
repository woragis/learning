from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import date
from uuid import uuid4
from api.models import Vehicle, Travel, UserRegistration


class UserRegistrationViewSetTest(APITestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(name="User Bus", capacity=40)
        self.travel = Travel.objects.create(
            name="User Event",
            date=date(2025, 5, 20),
            description="Event for registered users"
        )
        self.unique = {
            'username': f'user-{uuid4()}',
            'email': f'user-{uuid4()}@example.com',
        }
        self.user = UserRegistration.objects.create(
            name="John Doe",
            username=self.unique["username"],
            email=self.unique["email"],
            password="password123",
            has_paid=True,
            church_name="Church ABC",
            vehicle=self.vehicle,
            travel=self.travel
        )
        self.user_url = reverse("userregistration-detail", args=[self.user.id])
        self.user_list_url = reverse("userregistration-list")

    def test_list_users(self):
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {
            "name": "Jane Doe",
            "username": f"user-{uuid4()}",
            "email": f"user-{uuid4()}@example.com",
            "password": "password456",
            "has_paid": False,
            "church_name": "Church XYZ",
            "vehicle": self.vehicle.id,
            "travel": self.travel.id
        }
        response = self.client.post(self.user_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_user(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        data = {
            "name": "John Updated",
            "username": self.user.username,
            "email": self.user.email,
            "password": "newpass123",
            "has_paid": False,
            "church_name": "Updated Church",
            "vehicle": self.vehicle.id,
            "travel": self.travel.id
        }
        response = self.client.put(self.user_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, "John Updated")

    def test_delete_user(self):
        response = self.client.delete(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(UserRegistration.objects.filter(
            id=self.user.id).exists())
