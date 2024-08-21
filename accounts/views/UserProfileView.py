from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class UserProfileView(LoginRequiredMixin, TemplateView):
    """
        View for displaying the logged-in user's profile.

        This view requires that the user is logged in to access the profile page. It renders
        the user's profile information and includes custom context data for template rendering.

        Attributes:
            template_name (str): The path to the template used to render the user's profile.
    """
    template_name = 'accounts/profile.html'
