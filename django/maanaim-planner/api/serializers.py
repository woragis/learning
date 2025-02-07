from rest_framework import serializers
from .models import Vehicle, Travel, UserRegistration

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'