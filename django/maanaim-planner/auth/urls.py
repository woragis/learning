from .views import CustomTokenObtainPairView, CustomTokenRefreshView, ProtectedView, RegisterUserView
from django.urls import path

urlpatterns = [
    path(
        'login/',
        CustomTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'profile/',
        ProtectedView.as_view(),
        name='profile'
    ),
    path(
        'refresh/',
        CustomTokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'register/',
        RegisterUserView.as_view(),
        name='register'
    ),
]
