from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .vehicle import Vehicle
from .travel import Travel


class User(AbstractUser):
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
    email = models.EmailField(
        max_length=200,
        unique=True,
        blank=False,
        help_text="User's email for registration"
    )
    username = models.CharField(
        max_length=64,
        unique=True,
        blank=True,
        null=True,
        help_text="Unique username (optional)"
    )
    password = models.CharField(max_length=128)
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
        help_text=helpers['travel']
    )

    # 🚀 Fix related_name conflict
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )

    class Meta:
        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["travel"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["email", "travel"], name="unique_email_per_travel")
        ]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f'{self.name} - {self.travel.name} - {self.get_vehicle_name()}'

    def get_vehicle_name(self):
        return self.vehicle.name if self.vehicle else "No Vehicle"

    def clean(self):
        if not self.email and not self.username:
            raise ValidationError(
                _("Either an email or a username is required."))

    def save(self, *args, **kwargs):
        self.clean()
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)
