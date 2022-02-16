from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """User Custom !"""

    GENDER_MEN = "man"
    GENDER_WOMAN = "woman"

    """ CharField에서 select문처럼 옵션추가하는거 비슷한거"""
    GENDER_CHOICES = (
        (GENDER_MEN, "Male"),
        (GENDER_WOMAN, "Female"),
    )

    """UserCustom Model"""

    biometric = models.TextField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    superhost = models.BooleanField(default=False)
