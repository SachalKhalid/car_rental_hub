from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import *


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
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username} ({self.role})'


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


# Car Model
class Car(models.Model):
    """
        Represents a car available for rent at a shop.

        Fields:
            car_brand: The brand of the car.
            model: The model of the car.
            year: The manufacturing year of the car.
            color: The color of the car.
            license_plate_number: The unique license plate number of the car.
            shop: A foreign key linking to the Shop model, indicating the shop where the car is available.
            availability_status: The current status of the car, such as 'Available', 'Rented', or 'Maintenance'.

        Methods:
             __str__: Returns a string representation of the car, including its brand, model, and license plate number.
    """
    car_brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    license_plate_number = models.CharField(max_length=20, unique=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    availability_status = models.CharField(max_length=20, choices=AVAILABILITY_STATUS_CHOICES, default='Available')

    def __str__(self):
        return f'{self.car_brand} {self.model} ({self.license_plate_number})'


# Rental Model
class Rental(models.Model):
    """
        Represents a rental transaction for a car.

        Fields:
            shop: A foreign key linking to the Shop model, indicating the shop where the car is rented.
            car: A foreign key linking to the Car model, representing the car being rented.
            user: A foreign key linking to the User model, representing the customer getting the car.
            rental_start_date: The start date of the rental period.
            rental_end_date: The end date of the rental period.
            total_cost: The total cost of the rental car.

        Methods:
            __str__: Returns a string representation of the rental, including the rented car and the user.
    """
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Rented {self.car} to {self.user}'


# Review Model
class Review(models.Model):
    """
    Represents a review for a rented car.

    Fields:
        car: A foreign key linking to the Car model, indicating the car being reviewed.
        user: A foreign key linking to the User model, indicating the user who wrote the review.
        rating: The rating given to the car, having rating choice form 1 to 5
        comment: A text comment provided by the user about the car.
        date: The date and time when the review was created.

    Methods:
        __str__: Returns a string representation of the review, including the reviewed car and the
                user who wrote the review.
    """

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_RANGE)
    comment = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review to {self.car} by {self.user}'
