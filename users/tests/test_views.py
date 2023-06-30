from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from users.models import CustomUser


class UserRegistrationViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_new_user(self):
        url = reverse('register')
        data = {
            'name': 'Test User',
            'email': 'test1@test.com',
            'password': 'testpass123',
            'membership_type': 'R',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('refresh' in response.json())
        self.assertTrue('access' in response.json())
        self.assertTrue(CustomUser.objects.filter(email='test1@test.com').exists())

    def test_register_existing_user(self):
        url = reverse('register')
        data = {
            'name': 'Test User',
            'email': 'test5@test.com',
            'password': 'testpass123',
            'membership_type': 'R',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserLoginViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            name='Test User',
            email='test3@test.com',
            password='testpass123',
            membership_type='R',
        )

    def test_login_existing_user(self):
        url = reverse('login')
        data = {
            'email': 'test3@test.com',
            'password': 'testpass123',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('refresh' in response.json())
        self.assertTrue('access' in response.json())

    def test_login_non_existing_user(self):
        url = reverse('login')
        data = {'email': 'nonexisting@test.com', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_wrong_password(self):
        url = reverse('login')
        data = {
            'email': 'test3@test.com',
            'password': 'wrongpass123',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserLogoutViewTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='testpassword'
        )
        self.refresh_token = str(RefreshToken.for_user(self.user))

    def test_logout_with_valid_token(self):
            refresh = RefreshToken.for_user(self.user)
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}') # type: ignore
            url = reverse('logout')
            response = self.client.post(url, {'refresh': str(refresh)}, format='json')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertTrue(BlacklistedToken.objects.filter(token__jti=refresh.payload['jti']).exists())

    def test_logout_with_invalid_token(self):
        url = reverse('logout')
        data = {'refresh': 'invalid_token'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_without_token(self):
        url = reverse('logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)