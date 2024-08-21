from django.contrib.auth.forms import UserCreationForm
from accounts.constants import *
from accounts.models import User


class UserAccountCreationForm(UserCreationForm):
    """
        A custom form for creating a new user account with additional fields.

        This form extends the built-in UserCreationForm to include additional fields such as
        phone number, role, and address. It is used to handle user registration by providing
        a form that collects all necessary information and validates it.

        Meta:
            model: The model associated with this form is the `User` model.
            fields: A list of fields to be included in the form.
    """

    class Meta:
        model = User
        fields = USER_CREATION_FORM_FIELDS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].choices = PUBLIC_USER_ROLE_CHOICES
