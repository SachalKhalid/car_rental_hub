from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from accounts.constants import *
from accounts.models import User

class UpdateUserView(LoginRequiredMixin, UpdateView):
    """
       View to update a user's details.

       This view requires the user to be logged in. Upon successfully updating the user details,
       it redirects to the profile page.

       Attributes:
           model (Model): The model to use for the update view, which is the User model.
           fields (list): The fields of the User model that can be updated.
           template_name (str): The name of the template to use for rendering the update form.
           success_url (str): The URL to redirect to upon successful form submission.
    """
    model = User
    fields = FIELDS
    template_name = 'accounts/update_user.html'
    success_url = reverse_lazy(PROFILE)
