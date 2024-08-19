from django.db import models

from accounts.models import User


# Create your models here.


# Shop Model
class Shop(models.Model):
    """
    Represents a shop that rents out cars.

    Fields:
        name: The name of the shop.
        address: The physical address of the shop.
        phone_number: The contact phone number of the shop.
        owner: A foreign key linking to the User model, representing the owner of the shop.

    Methods:
        __str__: Returns the name of the shop.
    """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
