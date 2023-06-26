from django.test import TestCase
from users.models import CustomUser
from users.views import EmailBackend

class EmailBackendTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            name='Test User',
            email='test@test.com',
            password='testpass123',
            membership_type='R',
        )
        self.backend = EmailBackend()

    def test_authenticate_valid_credentials(self):
        user = self.backend.authenticate(None, email='test@test.com', password='testpass123')
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@test.com') # type: ignore

    def test_authenticate_invalid_email(self):
        user = self.backend.authenticate(None, email='nonexisting@test.com', password='testpass123')
        self.assertIsNone(user)

    def test_authenticate_invalid_password(self):
        user = self.backend.authenticate(None, email='test@test.com', password='wrongpass123')
        self.assertIsNone(user)
