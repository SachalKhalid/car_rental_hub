from django.db import models

from accounts.models import User
from cars.models import Car
from shops.models import Shop


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
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Rented {self.car} to {self.user}'
