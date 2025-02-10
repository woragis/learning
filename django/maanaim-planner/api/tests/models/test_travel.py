from django.test import TestCase
from datetime import date
from api.models.travel import Travel


class TravelModelTest(TestCase):
    def test_travel_creation(self):
        # Create a travel event
        travel = Travel.objects.create(
            name='Weekly Travel',
            date=date(2023, 10, 15),
            description='Travel to the main church'
        )

        # Check if the travel event was created successfully
        self.assertEqual(travel.name, 'Weekly Travel')
        self.assertEqual(travel.date.strftime('%Y-%m-%d'), '2023-10-15')
        self.assertEqual(travel.description, 'Travel to the main church')

    def test_travel_str_representation(self):
        # Create a travel event
        travel = Travel.objects.create(
            name='Monthly Travel',
            date=date(2023, 11, 1)
        )

        # Check the string representation
        self.assertEqual(str(travel), 'Monthly Travel - 2023-11-01')
