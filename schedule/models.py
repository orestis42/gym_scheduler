from django.db import models
from datetime import timedelta

class Slot(models.Model):
    DAY_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]

    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.IntegerField(choices=DAY_CHOICES)
    regular_slots = models.IntegerField(default=6)
    premium_slots = models.IntegerField(default=3)

    def default_slot(self):
        return Slot.objects.get_or_create(day_of_week=1, start_time='10:00', end_time='11:00', regular_slots=1, premium_slots=1)[0]


    @classmethod
    def generate_slots(cls, start_time, end_time, interval_minutes):
        """Generate slots for each day based on the gym's operating hours."""
        slots = []
        time = start_time
        while time < end_time:
            for day in range(6):  # Generate slots for Monday to Saturday
                slot = cls(start_time=time, end_time=(time + timedelta(minutes=interval_minutes)), day_of_week=day)
                slots.append(slot)
            time += timedelta(minutes=interval_minutes)
        cls.objects.bulk_create(slots)