from django.db import models
from django.core.exceptions import ValidationError
from users.models import CustomUser
from schedule.models import Slot

def default_slot():
    return Slot.objects.get_or_create(day_of_week=1, start_time='10:00', end_time='11:00', regular_slots=1, premium_slots=1)[0]

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name='bookings', default=default_slot)
    booking_type = models.CharField(max_length=1, choices=[('R', 'Regular'), ('P', 'Premium')], default='R')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'slot'],
                name='unique_booking_for_user_per_slot',
            ),
        ]

    def clean(self):
        super().clean()

        # Check that user's membership type matches the booking type
        if self.user.membership_type != self.booking_type:
            raise ValidationError("User's membership type must match booking type.")

        # Check that user does not exceed maximum of 2 slots per day
        same_day_bookings = Booking.objects.filter(user=self.user, slot__day_of_week=self.slot.day_of_week)
        if same_day_bookings.count() >= 2:
            raise ValidationError("A user can book up to 2 slots per day.")

    def save(self, *args, **kwargs):
        self.clean()

        regular_bookings = Booking.objects.filter(slot=self.slot, booking_type='R').count()
        premium_bookings = Booking.objects.filter(slot=self.slot, booking_type='P').count()

        if self.booking_type == 'R' and regular_bookings >= self.slot.regular_slots:
            raise ValidationError("No more regular slots available for this time slot.")
        elif self.booking_type == 'P' and premium_bookings >= self.slot.premium_slots:
            raise ValidationError("No more premium slots available for this time slot.")

        return super(Booking, self).save(*args, **kwargs)
