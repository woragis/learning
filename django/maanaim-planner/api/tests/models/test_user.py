from django.test import TestCase
from django.core.exceptions import ValidationError
from ...models import Vehicle, Travel, UserRegistration


class UserRegistrationModelTest(TestCase):
    def setUp(self):
        # Create test data
        self.vehicle = Vehicle.objects.create(name='Van 1', capacity=2)
        self.travel = Travel.objects.create(
            name='Weekly Travel',
            date='2023-10-15'
        )

    def test_user_registration_creation(self):
        # Create a user registration
        registration = UserRegistration.objects.create(
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
        registration = UserRegistration.objects.create(
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
        UserRegistration.objects.create(
            username='User 1',
            church_name='Mangabeira',
            has_paid=True,
            vehicle=self.vehicle,
            travel=self.travel
        )

        # Create another registration for the same vehicle and travel
        UserRegistration.objects.create(
            username='User 2',
            church_name='Mangabeira',
            has_paid=True,
            vehicle=self.vehicle,
            travel=self.travel
        )

        # Attempt to create a third registration (should fail due to capacity)
        with self.assertRaises(ValidationError):
            registration = UserRegistration(
                username='User 3',
                church_name='Mangabeira',
                has_paid=True,
                vehicle=self.vehicle,
                travel=self.travel
            )
            registration.full_clean()  # Trigger validation

    def test_user_registration_without_vehicle(self):
        # Create a user registration without a vehicle
        registration = UserRegistration.objects.create(
            username='User 4',
            church_name='Mangabeira',
            has_paid=False,
            travel=self.travel
        )

        # Check if the registration was created successfully
        self.assertIsNone(registration.vehicle)
