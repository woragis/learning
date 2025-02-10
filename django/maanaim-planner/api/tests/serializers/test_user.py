from datetime import date
from django.test import TestCase
from api.models import UserRegistration
from api.serializers import UserRegistrationSerializer


class UserRegistrationSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "securepassword"
        }
        self.user = UserRegistration.objects.create(**self.user_data)

    def test_user_serialization(self):
        serializer = UserRegistrationSerializer(instance=self.user)
        expected_data = {
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "securepassword"
        }
        self.assertEqual(serializer.data, expected_data)

    def test_user_deserialization(self):
        serializer = UserRegistrationSerializer(data={
            "username": "janedoe",
            "email": "janedoe@example.com",
            "password": "anothersecurepassword"
        })
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["username"], "janedoe")
