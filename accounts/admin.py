from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .forms import *
from accounts.constants import *
from accounts.models import User


# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = (
        (USER_CREDENTIALS_LABEL, {'fields': USER_CREDENTIALS_FIELDS}),
        (PERSONAL_INFO_LABEL, {'fields': PERSONAL_INFO_FIELDS}),
        (IMPORTANT_DATES_LABEL, {'fields': IMPORTANT_DATES_FIELDS}),
    )

    # Define the fieldsets for the add user view
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': USER_CREATION_FORM_FIELDS,
        }),
    )

    ordering = ORDERING_FIELDS


admin.site.register(User, CustomUserAdmin)
