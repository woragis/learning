
from django.db import models
from django.core.exceptions import ValidationError


# Vehicle Model
class Vehicle(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='Name of the vehicle'
    )
    capacity = models.PositiveIntegerField(
        help_text='Maximum number of passengers the vehicle can hold'
    )

    def __str__(self):
        return self.name
