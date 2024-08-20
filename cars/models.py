from django.db import models

from cars.constants import AVAILABILITY_STATUS_CHOICES
from shops.models import Shop


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
            price: The price of the car
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
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    availability_status = models.CharField(max_length=20, choices=AVAILABILITY_STATUS_CHOICES, default='Available')

    def __str__(self):
        return f'{self.car_brand} {self.model} ({self.license_plate_number})'
