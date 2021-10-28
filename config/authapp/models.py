from django.db import models

from django.contrib.auth.models import AbstractUser

from .manager import UserManager

# Create your models here.
class User(AbstractUser):
    username=None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    age = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
