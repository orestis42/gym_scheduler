from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.exceptions import ValidationError
from ..models import CustomUser
from ..serializers import UserRegistrationSerializer

class UserRegistrationSerializerTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_valid_data(self):
        data = {
            'email': 'test@example.com',
            'password': 'strongpassword123',
            'name': 'Test User',
            'membership_type': CustomUser.REGULAR,
        }
        serializer = UserRegistrationSerializer(data=data) #type: ignore
        self.assertTrue(serializer.is_valid())

        user = serializer.save()
        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.name, data['name'])
        self.assertTrue(user.check_password(data['password']))
        self.assertEqual(user.membership_type, data['membership_type'])

    def test_missing_field(self):
        data = {
            'email': 'test@example.com',
            'password': 'strongpassword123',
            'name': 'Test User',
        }
        serializer = UserRegistrationSerializer(data=data) #type: ignore
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_invalid_email(self):
        data = {
            'email': 'not an email',
            'password': 'strongpassword123',
            'name': 'Test User',
            'membership_type': CustomUser.REGULAR,
        }
        serializer = UserRegistrationSerializer(data=data) #type: ignore
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_weak_password(self):
        data = {
            'email': 'test@example.com',
            'password': 'weak',
            'name': 'Test User',
            'membership_type': CustomUser.REGULAR,
        }
        serializer = UserRegistrationSerializer(data=data) #type: ignore
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_empty_name(self):
            data = {
                'email': 'test@example.com',
                'password': 'strongpassword123',
                'name': '',
                'membership_type': CustomUser.REGULAR,
            }
            serializer = UserRegistrationSerializer(data=data) #type: ignore
            with self.assertRaises(ValidationError):
                serializer.is_valid(raise_exception=True)

    def test_invalid_membership_type(self):
        data = {
            'email': 'test@example.com',
            'password': 'strongpassword123',
            'name': 'Test User',
            'membership_type': 'Invalid',
        }
        serializer = UserRegistrationSerializer(data=data) #type: ignore
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_duplicate_email(self):
        data1 = {
            'email': 'test@example.com',
            'password': 'strongpassword123',
            'name': 'Test User 1',
            'membership_type': CustomUser.REGULAR,
        }
        serializer1 = UserRegistrationSerializer(data=data1) #type: ignore
        self.assertTrue(serializer1.is_valid())
        serializer1.save()

        data2 = {
            'email': 'test@example.com',
            'password': 'strongpassword123',
            'name': 'Test User 2',
            'membership_type': CustomUser.REGULAR,
        }
        serializer2 = UserRegistrationSerializer(data=data2) #type: ignore
        with self.assertRaises(ValidationError):
            serializer2.is_valid(raise_exception=True)

    def test_empty_email(self):
        data = {
            'email': '',
            'password': 'strongpassword123',
            'name': 'Test User',
            'membership_type': CustomUser.REGULAR,
        }
        serializer = UserRegistrationSerializer(data=data) #type: ignore
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_empty_password(self):
        data = {
            'email': 'test@example.com',
            'password': '',
            'name': 'Test User',
            'membership_type': CustomUser.REGULAR,
        }
        serializer = UserRegistrationSerializer(data=data) #type: ignore
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)