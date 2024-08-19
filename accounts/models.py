from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.constants import *


# User Model
class User(AbstractUser):
    """
        A user class which have all Existing fields and methods of AbstractUser
        and some additional fields.

        Fields:
            role: The role of the user, which could be 'Customer', 'Admin', or 'ShopOwner'.
            phone_number: The user's phone number.
            address: The user's address.

        Methods:
            __str__: Returns a string representation of the user, including their username and role.
    """
    role = models.CharField(max_length=20, choices=ADMIN_USER_ROLE_CHOICES)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username} ({self.role})'
