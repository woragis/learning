from django.test import TestCase
from django.core.exceptions import ValidationError
from api.models.vehicle import Vehicle


class VehicleModelTest(TestCase):
    def test_vehicle_creation(self):
        # Create a vehicle
        vehicle = Vehicle.objects.create(name='Bus 1', capacity=50)

        # Check if the vehicle was created successfully
        self.assertEqual(vehicle.name, 'Bus 1')
        self.assertEqual(vehicle.capacity, 50)

    def test_vehicle_str_representation(self):
        # Create a vehicle
        vehicle = Vehicle.objects.create(name='Bus 2', capacity=30)

        # Check the string representation
        self.assertEqual(str(vehicle), 'Bus 2')
