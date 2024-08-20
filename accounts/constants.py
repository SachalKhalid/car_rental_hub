# All user roles, including 'Admin', 'Customer', and 'ShopOwner'.
# These are typically used in the admin panel where an administrator has the privilege to assign any role.
ADMIN_USER_ROLE_CHOICES = [
    ('Customer', 'Customer'),  # Regular user of the application
    ('Admin', 'Admin'),  # Administrator with higher privileges
    ('ShopOwner', 'ShopOwner'),  # User who owns and manages a shop
]

# Restricted user roles available to the public.
# These are used in public-facing registration forms where the 'Admin' role is excluded.
PUBLIC_USER_ROLE_CHOICES = [
    ('Customer', 'Customer'),  # Regular user of the application
    ('ShopOwner', 'ShopOwner'),  # User who owns and manages a shop
]

# String constant representing the 'Admin' role. Used for comparison and checks.
ADMIN = 'Admin'

# The name of the context variable used in templates to pass the list of users.
USERS_LIST = 'users_list'

# List of fields used in user-related forms and views. Represents fields for user update.
FIELDS = ['username', 'email', 'phone_number', 'role', 'address']

# List of fields used in the user creation form.
USER_CREATION_FORM_FIELDS = ['username', 'email', 'phone_number', 'role', 'address', 'password1', 'password2']

# The attribute name for the authenticated user instance in forms.
AUTHENTICATED_USER = 'user'

# URL name for the user profile and login page. Used in URL reversing and template URL lookups.
PROFILE = 'profile'
LOGIN = 'login'

# The field name for the user's email address  and password in forms and validation logic.
USER_EMAIL_FIELD = 'email'
USER_PASSWORD_FIELD = 'password'

# Constants for form field labels
EMAIL_FIELD_LABEL = 'Email'
PASSWORD_FIELD_LABEL = 'Password'
