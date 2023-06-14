from django.contrib.auth.models import User
from django.db import models

class MembershipType(models.TextChoices):
    REGULAR = 'R', 'Regular'
    PREMIUM = 'P', 'Premium'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.CharField(
        max_length=2,
        choices=MembershipType.choices,
        default=MembershipType.REGULAR,
    )

    def __str__(self):
        return self.user.username
