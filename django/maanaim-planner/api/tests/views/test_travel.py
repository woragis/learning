from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Travel


class TravelViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.travel_data = {"name": "Weekend Trip",
                            "date": "2023-10-15", "description": "Trip to the mountains."}
        self.travel = Travel.objects.create(**self.travel_data)

    def test_get_travels(self):
        response = self.client.get("/travels/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
