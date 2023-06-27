from django.test import TestCase, RequestFactory
from unittest.mock import patch, Mock
from django.http import Http404
from users.models import CustomUser
from users.views import EmailBackend

class EmailBackendTest(TestCase):
    def setUp(self):
        self.backend = EmailBackend()
        self.factory = RequestFactory()

    @patch('users.views.get_object_or_404')
    def test_authenticate_with_valid_credentials(self, mock_get):
        mock_user = Mock(spec=CustomUser)
        mock_user.check_password.return_value = True
        mock_get.return_value = mock_user

        request = self.factory.get('/login')
        user = self.backend.authenticate(request, email='test@example.com', password='test_password')

        mock_get.assert_called_once_with(CustomUser, email='test@example.com')
        mock_user.check_password.assert_called_once_with('test_password')
        self.assertEqual(user, mock_user)

    @patch('users.views.get_object_or_404')
    def test_authenticate_with_invalid_password(self, mock_get):
        mock_user = Mock(spec=CustomUser)
        mock_user.check_password.return_value = False
        mock_get.return_value = mock_user

        request = self.factory.get('/login')
        user = self.backend.authenticate(request, email='test@example.com', password='wrong_password')

        mock_get.assert_called_once_with(CustomUser, email='test@example.com')
        mock_user.check_password.assert_called_once_with('wrong_password')
        self.assertIsNone(user)

    @patch('users.views.get_object_or_404')
    def test_authenticate_with_nonexistent_user(self, mock_get):
        mock_get.side_effect = Http404

        request = self.factory.get('/login')
        with self.assertRaises(Http404):
            self.backend.authenticate(request, email='nonexistent@example.com', password='test_password')

        mock_get.assert_called_once_with(CustomUser, email='nonexistent@example.com')
