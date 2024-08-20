from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView

from .constants import *
from .forms import UserAccountCreationForm, EmailAuthenticationForm
from .models import User


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


class UserLogoutView(LogoutView):
    """
        View for user logout.

        This view logs out the user and redirects them to the login page.

        Attributes:
            next_page: The URL to redirect to after logout (login page).
    """
    next_page = reverse_lazy(LOGIN)


class UserProfileView(LoginRequiredMixin, TemplateView):
    """
        View for displaying the logged-in user's profile.

        This view requires that the user is logged in to access the profile page. It renders
        the user's profile information and includes custom context data for template rendering.

        Attributes:
            template_name (str): The path to the template used to render the user's profile.
    """
    template_name = 'accounts/profile.html'


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
