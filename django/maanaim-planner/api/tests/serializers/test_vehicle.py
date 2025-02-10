from datetime import date
from django.test import TestCase
from api.models import Vehicle
from api.serializers import VehicleSerializer


class VehicleSerializerTest(TestCase):
    def setUp(self):
        self.vehicle_data = {
            "name": "Bus A",
            "plate_number": "ABC-1234",
            "capacity": 50
        }
        self.vehicle = Vehicle.objects.create(**self.vehicle_data)

    def test_vehicle_serialization(self):
        serializer = VehicleSerializer(instance=self.vehicle)
        self.assertEqual(serializer.data, self.vehicle_data)

    def test_vehicle_deserialization(self):
        serializer = VehicleSerializer(data=self.vehicle_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(
            serializer.validated_data["name"], self.vehicle_data["name"])
