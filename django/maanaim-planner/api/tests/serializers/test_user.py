from datetime import date
from uuid import uuid4
from django.test import TestCase
from api.models.travel import Travel
from api.models.vehicle import Vehicle
from api.models.user import UserRegistration
from api.serializers import UserRegistrationSerializer


class UserRegistrationSerializerTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            name='Carro de Antonini',
            capacity=2,
        )

        self.travel = Travel.objects.create(
            name='Maanaim Grupo de Louvor - PE',
            date=date(2025, 2, 8),
            description='Maanaim feito para aprender sobre a doutrina do louvor e ver darla',
        )

        # Generate unique username and email for setUp
        self.user_data = {
            'name': 'johndoe',
            'username': str(uuid4()),  # Unique username
            'email': f'{uuid4()}@example.com',  # Unique email
            'password': 'password',
            'has_paid': True,
            'church_name': 'Cidade Verde',
            'vehicle': self.vehicle,
            'travel': self.travel,
        }
        self.user = UserRegistration.objects.create(**self.user_data)

    def test_user_serialization(self):
        serializer = UserRegistrationSerializer(instance=self.user)
        self.assertEqual(serializer.data['name'], self.user_data['name'])
        self.assertEqual(
            serializer.data['username'], self.user_data['username'])
        self.assertEqual(serializer.data['email'], self.user_data['email'])
        self.assertEqual(
            serializer.data['password'], self.user_data['password'])
        self.assertEqual(
            serializer.data['church_name'], self.user_data['church_name'])

    def test_user_deserialization(self):
        # Generate unique username and email for deserialization test
        unique_username = str(uuid4())
        unique_email = f'{uuid4()}@example.com'

        serializer = UserRegistrationSerializer(data={
            'name': 'janedoe',  # Fixing the assertion issue
            'username': unique_username,  # New unique username
            'email': unique_email,  # New unique email
            'password': 'password',
            'has_paid': True,
            'church_name': 'Cidade Verde',
            'vehicle': self.vehicle.id,  # Pass the ID instead of object
            'travel': self.travel.id,  # Pass the ID instead of object
        })

        if not serializer.is_valid():
            with open('log/tests/errors/serialization/user_error.txt', 'w') as f:
                f.write(str(serializer.errors))

        self.assertTrue(serializer.is_valid())
        # Fixing the expected value
        self.assertEqual(serializer.validated_data['name'], 'janedoe')
