from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from accounts.constants import *


class EmailAuthenticationForm(forms.Form):
    """
        A custom authentication form that uses email and password for user authentication.

        This form is designed to authenticate users based on their email and password.
        It validates the credentials and checks if the user is active.

        Fields:
            email: A form field for the user's email address.
            password: A form field for the user's password.

        Methods:
            __init__(*args, **kwargs): Initializes the form and sets up any additional parameters if needed.
            clean(): Validates the email and password. Authenticates the user and raises validation errors if the
                        credentials are invalid or if the user is inactive.
            get_user(): Returns the authenticated user instance if authentication is
                        successful; otherwise, returns `None`.
    """

    email = forms.EmailField(
        label=EMAIL_FIELD_LABEL
    )
    password = forms.CharField(
        label=PASSWORD_FIELD_LABEL,
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        """
            Initializes the form and sets up any additional parameters if needed.
        """
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        """
            Validate the email and password and authenticate the user.
        """
        email = self.cleaned_data.get(USER_EMAIL_FIELD)
        password = self.cleaned_data.get(USER_PASSWORD_FIELD)

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise ValidationError("Invalid email or password (User is not authenticated)")
            self.user = user
        return self.cleaned_data

    def get_user(self):
        return getattr(self, AUTHENTICATED_USER)
