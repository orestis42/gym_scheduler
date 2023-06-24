from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import CustomUser

class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            name='Test User',
            email='test@test.com',
            password='testpass123',
            membership_type='R',
        )

        self.superuser = CustomUser.objects.create_superuser(
            name='Super User',
            email='super@test.com',
            password='testpass123',
        )

    def test_user_creation(self):
        self.assertEqual(f'{self.user.name}', 'Test User')
        self.assertEqual(f'{self.user.email}', 'test@test.com')
        self.assertEqual(f'{self.user.membership_type}', 'R')

    def test_superuser_creation(self):
        self.assertEqual(f'{self.superuser.name}', 'Super User')
        self.assertEqual(f'{self.superuser.email}', 'super@test.com')
        self.assertTrue(self.superuser.is_superuser)
        self.assertTrue(self.superuser.is_staff)

    def test_default_membership_type(self):
        user = CustomUser.objects.create_user(
            name='Test User 2',
            email='test2@test.com',
            password='testpass123',
        )
        self.assertEqual(f'{user.membership_type}', 'R')