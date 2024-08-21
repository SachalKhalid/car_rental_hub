from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from accounts.constants import *
from accounts.models import User

class UserListView(LoginRequiredMixin, ListView):
    """
        View for displaying a list of users.

        This view is accessible only to logged-in users who have the 'Admin' role. It displays
        a list of users using the specified template. The view inherits from `LoginRequiredMixin`
        to ensure that only authenticated users can access the list of users.

        Attributes:
            model (Model): The model to use for the list view, which is the User model.
            template_name (str): The path to the template used to render the list of users.
            context_object_name (str): The name of the context variable that will contain
                                        the list of users in the template, set to USERS_LIST.
    """
    model = User
    template_name = 'accounts/user_list.html'
    context_object_name = USERS_LIST