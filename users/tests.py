from django.contrib.auth.models import User
from django.test import TestCase
from .models import UserProfile, MembershipType

class UserProfileModelTest(TestCase):
    def setUp(self):
        # Create a User and UserProfile for use in the tests
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user, membership_type=MembershipType.REGULAR)

    def test_create_user_profile(self):
        # Retrieve the UserProfile
        user_profile = UserProfile.objects.get(user=self.user)

        # Check that the UserProfile was created correctly
        self.assertEqual(user_profile.user.username, 'testuser')
        self.assertEqual(user_profile.membership_type, MembershipType.REGULAR)

    def test_change_membership_type(self):
        # Change the membership type
        self.user_profile.membership_type = MembershipType.PREMIUM
        self.user_profile.save()

        # Retrieve the updated UserProfile
        updated_user_profile = UserProfile.objects.get(user=self.user)

        # Check that the membership type was updated correctly
        self.assertEqual(updated_user_profile.membership_type, MembershipType.PREMIUM)

    def test_str_method(self):
        # Check the output of the __str__ method
        self.assertEqual(str(self.user_profile), 'testuser')
