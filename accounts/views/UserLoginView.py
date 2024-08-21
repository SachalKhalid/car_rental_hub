from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from accounts.constants import *
from accounts.forms.EmailAuthenticationForm import EmailAuthenticationForm


class UserLoginView(FormView):
    """
        View for user login using email and password.

        This view presents a login form where users can enter their email and password to log in.
        Upon successful login, the user is redirected to their profile page.

        Attributes:
            template_name: The template used to render the login form.
            form_class: The form class used for authentication (EmailAuthenticationForm).
            success_url: The URL to redirect to upon successful login (user's profile page).

        Methods:
            form_valid(form): Logs in the user upon successful form validation and redirects to success_url.
    """
    template_name = 'accounts/login.html'
    form_class = EmailAuthenticationForm
    success_url = reverse_lazy(PROFILE)

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
