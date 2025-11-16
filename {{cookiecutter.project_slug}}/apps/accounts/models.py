from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile_number = models.CharField(
        max_length=32,
        blank=True,
        help_text="Mobile number for optional SMS 2FA.",
    )

    onboarding_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.get_username()
