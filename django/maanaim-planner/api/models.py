from django.db import models
from django.core.exceptions import ValidationError


# Vehicle Model
class Vehicle(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            help_text='Name of the vehicle')
    capacity = models.PositiveIntegerField(
        help_text='Maximum number of passengers the vehicle can hold')

    def __str__(self):
        return self.name


# Travel Model
class Travel(models.Model):
    name = models.CharField(
        max_length=100, help_text='Name of the travel event (e.g., Weekly Travel)')
    date = models.DateField(help_text='Date of the travel event')
    description = models.TextField(
        blank=True, null=True, help_text='Additional details about the travel')

    def __str__(self):
        return f'{self.name} - {self.date}'


# User Registration Model
class UserRegistration(models.Model):
    helpers = {
        'name': 'Name of the user registering for the travel',
        'church': 'Name of the user\'s church',
        'has_paid': 'Whether the user has paid for the travel or not',
        'vehicle': 'Vehicle selected by the user',
        'travel': 'Travel event the user is registering for',
    }
    defaults = {
        'church': 'Mangabeira'
    }

    name = models.CharField(max_length=100, help_text=helpers['name'])
    username = models.CharField(
        max_length=64, unique=True, null=True, blank=True)
    email = models.EmailField(
        max_length=200, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, default='password')
    church_name = models.CharField(
        max_length=100,
        help_text=helpers['church'],
        default=defaults['church']
    )
    has_paid = models.BooleanField(
        default=False,
        help_text=helpers['has_paid']
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text=helpers['vehicle']
    )
    travel = models.ForeignKey(
        Travel,
        on_delete=models.CASCADE,
        help_text=helpers['travel'],
    )

    def __str__(self):
        return f'{self.name} - {self.travel.name} - {self.vehicle}'

    def clean(self):
        # Check if the vehicle is already at capacity
        if self.vehicle:
            # Count the number of registrations for this vehicle and travel
            registrations_count = UserRegistration.objects.filter(
                vehicle=self.vehicle,
                travel=self.travel
            ).count()

            if registrations_count >= self.vehicle.capacity:
                raise ValidationError(
                    f'The vehicle \'{self.vehicle.name}\' is already full for this travel.')

    def save(self, *args, **kwargs):
        # Run validation before saving
        self.clean()
        super().save(*args, **kwargs)
