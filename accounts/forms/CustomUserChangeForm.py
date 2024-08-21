from django.contrib.auth.forms import UserChangeForm
from accounts.constants import *
from accounts.models import User


class CustomUserChangeForm(UserChangeForm):
    """
    Specify the user model edited while editing a user on the
    admin page.
    """

    class Meta:
        model = User
        fields = FIELDS
