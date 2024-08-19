from django.db import models

from accounts.models import User
from cars.models import Car
from reviews.constants import RATING_RANGE


# Create your models here.

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
