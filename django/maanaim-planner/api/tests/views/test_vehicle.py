from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Vehicle


class VehicleViewSetTest(APITestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(name="Bus A", capacity=50)
        self.vehicle_url = reverse("vehicle-detail", args=[self.vehicle.id])
        self.vehicle_list_url = reverse("vehicle-list")

    def test_list_vehicles(self):
        response = self.client.get(self.vehicle_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vehicle(self):
        data = {"name": "Bus B", "capacity": 60}
        response = self.client.post(self.vehicle_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_vehicle(self):
        response = self.client.get(self.vehicle_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_vehicle(self):
        data = {"name": "Updated Bus", "capacity": 55}
        response = self.client.put(self.vehicle_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vehicle.refresh_from_db()
        self.assertEqual(self.vehicle.name, "Updated Bus")

    def test_delete_vehicle(self):
        response = self.client.delete(self.vehicle_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Vehicle.objects.filter(id=self.vehicle.id).exists())
