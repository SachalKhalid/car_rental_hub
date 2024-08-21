from django.contrib.auth.forms import UserCreationForm
from accounts.constants import *
from accounts.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Specify the user model created while adding a user
    on the admin page.
    """

    class Meta:
        model = User
        fields = FIELDS
