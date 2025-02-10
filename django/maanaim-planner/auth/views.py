from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            "access": response.data["access"],
            "refresh": response.data["refresh"],
            "user": {
                "id": self.user.id,
                "name": self.user.name,
                "email": self.user.email,
            }
        }, status=status.HTTP_200_OK)


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            "access": response.data["access"],
            "refresh": response.data["refresh"],
            "user": {
                "id": self.user.id,
                "name": self.user.name,
                "email": self.user.email,
            }
        }, status=status.HTTP_200_OK)


class RegisterUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        if User.objects.filter(email=data["email"]).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            name=data["name"],
            email=data["email"],
            password=data["password"]
        )
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
            }
        }, status=status.HTTP_201_CREATED)


class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.name}!"})
