from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from accounts.constants import *


class UserLogoutView(LogoutView):
    """
        View for user logout.

        This view logs out the user and redirects them to the login page.

        Attributes:
            next_page: The URL to redirect to after logout (login page).
    """
    next_page = reverse_lazy(LOGIN)
