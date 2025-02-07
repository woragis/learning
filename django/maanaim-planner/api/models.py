from django.db import models
from django.core.exceptions import ValidationError


# Vehicle Model
class Vehicle(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Name of the vehicle')
    capacity = models.PositiveIntegerField(help_text='Maximum number of passengers the vehicle can hold')

    def __str__(self):
        return self.name


# Travel Model
class Travel(models.Model):
    name = models.CharField(max_length=100, help_text='Name of the travel event (e.g., Weekly Travel)')
    date = models.DateField(help_text='Date of the travel event')
    description = models.TextField(blank=True, null=True, help_text='Additional details about the travel')

    def __str__(self):
        return f'{self.name} - {self.date}'


# User Registration Model
class UserRegistration(models.Model):
    user_name = models.CharField(max_length=100, help_text='Name of the user registering for the travel')
    church_name = models.CharField(max_length=100, help_text='Name of the user\'s church', default='mangabeira')
    has_paid = models.BooleanField(default=False, help_text='Whether the user has paid for the travel')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True, help_text='Vehicle selected by the user')
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE, help_text='Travel event the user is registering for')

    def __str__(self):
        return f'{self.user_name} - {self.travel.name} - {self.vehicle}'

    def clean(self):
        # Check if the vehicle is already at capacity
        if self.vehicle:
            # Count the number of registrations for this vehicle and travel
            registrations_count = UserRegistration.objects.filter(
                vehicle=self.vehicle,
                travel=self.travel
            ).count()

            if registrations_count >= self.vehicle.capacity:
                raise ValidationError(f'The vehicle \'{self.vehicle.name}\' is already full for this travel.')

    def save(self, *args, **kwargs):
        # Run validation before saving
        self.clean()
        super().save(*args, **kwargs)