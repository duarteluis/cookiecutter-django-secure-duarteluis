from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import (
    LoginForm,
    SignupForm,
    ResetPasswordForm,
    ResetPasswordKeyForm,
)

User = get_user_model()
