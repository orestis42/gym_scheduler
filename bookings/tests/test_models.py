from django.test import TestCase
from django.contrib.auth.models import User
from bookings.models import Booking, TimeSlot
from users.models import UserProfile, MembershipType
from datetime import date, time, timedelta

class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create two users
        user1 = User.objects.create_user(username='user1', password='password')
        user2 = User.objects.create_user(username='user2', password='password')

        # Create user profiles
        UserProfile.objects.create(user=user1, membership_type=MembershipType.REGULAR)
        UserProfile.objects.create(user=user2, membership_type=MembershipType.PREMIUM)

        # Create a time slot
        cls.time_slot = TimeSlot.objects.create(start_time=time(9, 0), end_time=time(10, 0), day_of_week=1)

    def test_booking_conflicts(self):
        # Create a booking for user1
        booking1 = Booking.objects.create(user=User.objects.get(username='user1'), time_slot=self.time_slot, date=date.today())

        # Try to create a conflicting booking for user2
        booking2 = Booking(user=User.objects.get(username='user2'), time_slot=self.time_slot, date=date.today())

        self.assertTrue(booking2.conflicts_with_existing_booking())

    def test_booking_within_operating_hours(self):
        # Create a booking for user1
        booking = Booking.objects.create(user=User.objects.get(username='user1'), time_slot=self.time_slot, date=date.today())

        self.assertTrue(booking.is_working_hours())

    def test_booking_exceeds_daily_limit(self):
        # Create a booking for user1
        Booking.objects.create(user=User.objects.get(username='user1'), time_slot=self.time_slot, date=date.today())

        # Try to create another booking for user1 on the same day
        another_time_slot = TimeSlot.objects.create(start_time=time(10, 0), end_time=time(11, 0), day_of_week=1)
        another_booking = Booking(user=User.objects.get(username='user1'), time_slot=another_time_slot, date=date.today())

        self.assertTrue(another_booking.exceeds_daily_limit())

    def test_booking_exceeds_hourly_capacity(self):
        # Create six bookings for regular members in the same time slot
        for i in range(6):
            user = User.objects.create_user(username=f'regular{i}', password='password')
            UserProfile.objects.create(user=user, membership_type=MembershipType.REGULAR)
            Booking.objects.create(user=user, time_slot=self.time_slot, date=date.today())

        # Try to create another booking for a regular member in the same time slot
        another_user = User.objects.create_user(username='another_regular', password='password')
        UserProfile.objects.create(user=another_user, membership_type=MembershipType.REGULAR)
        another_booking = Booking(user=another_user, time_slot=self.time_slot, date=date.today())

        self.assertTrue(another_booking.exceeds_hourly_capacity())
