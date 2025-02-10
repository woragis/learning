from django.contrib import admin
from .models.travel import Travel
from .models.vehicle import Vehicle
from .models.user import User

admin.site.register(Vehicle)
admin.site.register(Travel)
admin.site.register(User)
