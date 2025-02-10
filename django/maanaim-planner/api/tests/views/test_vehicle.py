from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Vehicle


class VehicleViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vehicle_data = {"name": "Bus A",
                             "plate_number": "ABC-1234", "capacity": 50}
        self.vehicle = Vehicle.objects.create(**self.vehicle_data)

    def test_get_vehicles(self):
        response = self.client.get("/vehicles/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
