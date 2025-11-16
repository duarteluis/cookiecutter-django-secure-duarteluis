from django.urls import path
from apps.accounts.views.profile import ProfileView

app_name = "accounts_profile"

urlpatterns = [
    path("", ProfileView.as_view(), name="profile"),
]
