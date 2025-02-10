from django.db import models
from django.core.exceptions import ValidationError


# Travel Model
class Travel(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Name of the travel event (e.g., Weekly Travel)'
    )
    date = models.DateField(help_text='Date of the travel event')
    description = models.TextField(
        blank=True,
        null=True,
        help_text='Additional details about the travel'
    )

    def __str__(self):
        return f'{self.name} - {self.date}'
