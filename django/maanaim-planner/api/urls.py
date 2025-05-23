from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, TravelViewSet, UserViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'travels', TravelViewSet, basename='travel')
router.register(r'users', UserViewSet, basename='user')

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
