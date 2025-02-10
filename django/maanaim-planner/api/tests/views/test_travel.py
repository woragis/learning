from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import date
from api.models import Travel


class TravelViewSetTest(APITestCase):
    def setUp(self):
        self.travel = Travel.objects.create(
            name="Event X",
            date=date(2025, 2, 8),
            description="Music event for the youth"
        )
        self.travel_url = reverse("travel-detail", args=[self.travel.id])
        self.travel_list_url = reverse("travel-list")

    def test_list_travels(self):
        response = self.client.get(self.travel_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_travel(self):
        data = {
            "name": "Event Y",
            "date": "2025-03-10",
            "description": "Another event"
        }
        response = self.client.post(self.travel_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_travel(self):
        response = self.client.get(self.travel_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_travel(self):
        data = {"name": "Updated Event", "date": "2025-02-09",
                "description": "Updated desc"}
        response = self.client.put(self.travel_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.travel.refresh_from_db()
        self.assertEqual(self.travel.name, "Updated Event")

    def test_delete_travel(self):
        response = self.client.delete(self.travel_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Travel.objects.filter(id=self.travel.id).exists())
