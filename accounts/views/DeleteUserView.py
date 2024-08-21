from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from accounts.constants import *
from accounts.models import User


class DeleteUserView(LoginRequiredMixin, DeleteView):
    """
        View for handling the deletion of a user account.

        This view allow only authenticated users(admin) to delete user accounts. It presents
        a confirmation page before the deletion is performed to prevent accidental deletions.
        After the deletion is completed, the user is redirected to their profile page.

        Attributes:
            model (Model): The model associated with this view, which is the `User` model.
            template_name (str): The path to the template used to render the confirmation page.
            success_url (str): The URL to redirect to upon successful deletion of the user account.
                                This is typically the user's profile page.
        """
    model = User
    template_name = 'accounts/confirm_delete.html'
    success_url = reverse_lazy(PROFILE)
