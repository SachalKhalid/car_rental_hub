from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from accounts.constants import *
from accounts.forms.UserAccountCreationForm import UserAccountCreationForm
from accounts.models import User


class UserRegisterView(CreateView):
    """
       View for user registration.

       This view uses a form to create a new user and saves it to the database.
       After a successful registration, the user is redirected to the login page.

       Attributes:
           model: The User model.
           form_class: The form class used for user registration (UserAccountCreationForm).
           template_name: The template used to render the registration form.
           success_url: The URL to redirect to upon successful registration (login page).
    """
    model = User
    form_class = UserAccountCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy(LOGIN)
