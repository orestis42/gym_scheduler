from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from users.permissions import IsUnauthenticated
from users.models import CustomUser
from users.views import UserRegistrationView, UserLoginView
from django.contrib.auth.models import AnonymousUser

class IsUnauthenticatedTestCase(TestCase):
    def setUp(self):
        self.permission = IsUnauthenticated()
        self.user = CustomUser.objects.create_user(
            name='Test User',
            email='test3@test.com',
            password='testpass123',
            membership_type='R',
        )
        self.factory = APIRequestFactory()
        
        self.authenticated_request = self.factory.get('/')
        self.authenticated_request.user = self.user

        self.unauthenticated_request = self.factory.get('/')
        self.unauthenticated_request.user = AnonymousUser()

def test_authenticated_user_registration(self):
    has_permission = self.permission.has_permission(self.authenticated_request, UserRegistrationView())
    self.assertEqual(has_permission, False)

def test_unauthenticated_user_registration(self):
    has_permission = self.permission.has_permission(self.unauthenticated_request, UserRegistrationView())
    self.assertEqual(has_permission, True)

def test_authenticated_user_login(self):
    has_permission = self.permission.has_permission(self.authenticated_request, UserLoginView())
    self.assertEqual(has_permission, False)

def test_unauthenticated_user_login(self):
    has_permission = self.permission.has_permission(self.unauthenticated_request, UserLoginView())
    self.assertEqual(has_permission, True)
