from django.test import TestCase
from django.core.exceptions import ValidationError
from api.models.vehicle import Vehicle
from api.models.travel import Travel
from api.models.user import User


class UserModelTest(TestCase):
    def setUp(self):
        # Create test data
        self.vehicle = Vehicle.objects.create(name='Van 1', capacity=4)
        self.travel = Travel.objects.create(
            name='Weekly Travel',
            date='2023-10-15'
        )

    def test_user_registration_creation(self):
        # Create a user registration
        registration = User.objects.create(
            name='John Doe',
            username='woragis',
            email='jezreel@gmail.com',
            password='password',
            church_name='Mangabeira',
            has_paid=True,
            vehicle=self.vehicle,
            travel=self.travel
        )

        # Check if the registration was created successfully
        self.assertEqual(registration.name, 'John Doe')
        self.assertEqual(registration.church_name, 'Mangabeira')
        self.assertTrue(registration.has_paid)
        self.assertEqual(registration.vehicle, self.vehicle)
        self.assertEqual(registration.travel, self.travel)

    def test_user_registration_str_representation(self):
        # Create a user registration
        registration = User.objects.create(
            name='Jane Doe',
            username='woragis',
            email='admin@admin.com',
            password='password',
            church_name='Mangabeira',
            has_paid=False,
            vehicle=self.vehicle,
            travel=self.travel
        )

        # Check the string representation
        self.assertEqual(str(registration), 'Jane Doe - Weekly Travel - Van 1')

    def test_vehicle_capacity_validation(self):
        # Create a user registration
        User.objects.create(
            username='User 1',
            email='user1@email.com',
            password='password',
            church_name='Mangabeira',
            has_paid=True,
            vehicle=self.vehicle,
            travel=self.travel
        )

        # Create another registration for the same vehicle and travel
        User.objects.create(
            username='User 2',
            email='user2@email.com',
            password='password',
            church_name='Mangabeira',
            has_paid=True,
            vehicle=self.vehicle,
            travel=self.travel
        )

        # Attempt to create a third registration (should fail due to capacity)
        with self.assertRaises(ValidationError):
            registration = User(
                username='User 3',
                email='user3@email.com',
                password='password',
                church_name='Mangabeira',
                has_paid=True,
                vehicle=self.vehicle,
                travel=self.travel
            )
            registration.full_clean()  # Trigger validation

    def test_user_registration_without_vehicle(self):
        # Create a user registration without a vehicle
        registration = User.objects.create(
            username='User 4',
            email='user4@email.com',
            password='password',
            church_name='Mangabeira',
            has_paid=False,
            travel=self.travel
        )

        # Check if the registration was created successfully
        self.assertIsNone(registration.vehicle)
