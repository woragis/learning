from datetime import date
from django.test import TestCase
from api.models import Travel
from api.serializers import TravelSerializer


class TravelSerializerTest(TestCase):
    def setUp(self):
        self.travel_data = {
            "name": "Weekend Trip",
            "date": date(2023, 10, 15),
            "description": "Trip to the mountains."
        }
        self.travel = Travel.objects.create(**self.travel_data)

    def test_travel_serialization(self):
        serializer = TravelSerializer(instance=self.travel)
        expected_data = {
            "name": "Weekend Trip",
            "date": "2023-10-15",
            "description": "Trip to the mountains."
        }
        self.assertEqual(serializer.data, expected_data)

    def test_travel_deserialization(self):
        serializer = TravelSerializer(data={
            "name": "Beach Trip",
            "date": "2023-12-20",
            "description": "Trip to the beach."
        })
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["name"], "Beach Trip")
