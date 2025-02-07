from rest_framework import viewsets
from .models import Vehicle, Travel, UserRegistration
from .serializers import VehicleSerializer, TravelSerializer, UserRegistrationSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer