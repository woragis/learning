from django.contrib import admin
from .models import Vehicle, Travel, UserRegistration

admin.site.register(Vehicle)
admin.site.register(Travel)
admin.site.register(UserRegistration)