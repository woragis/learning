from datetime import date
from uuid import uuid4  # Import UUID for unique names
from django.test import TestCase
from api.models import Vehicle
from api.serializers import VehicleSerializer


class VehicleSerializerTest(TestCase):
    def setUp(self):
        self.vehicle_data = {
            "name": "Bus A I think",
            "capacity": 50
        }
        self.vehicle = Vehicle.objects.create(**self.vehicle_data)

    def test_vehicle_serialization(self):
        serializer = VehicleSerializer(instance=self.vehicle)
        self.assertEqual(serializer.data['name'], self.vehicle_data['name'])
        self.assertEqual(
            serializer.data['capacity'], self.vehicle_data['capacity'])

    def test_vehicle_deserialization(self):
        # Use a unique name to avoid duplicate errors
        unique_vehicle_data = {
            "name": f"Bus {uuid4()}",
            "capacity": 50
        }

        serializer = VehicleSerializer(data=unique_vehicle_data)

        if not serializer.is_valid():
            with open('log/tests/errors/serialization/vehicle_error.txt', 'w') as f:
                f.write(str(serializer.errors))

        self.assertTrue(serializer.is_valid())

        self.assertEqual(
            serializer.validated_data["name"], unique_vehicle_data["name"])
