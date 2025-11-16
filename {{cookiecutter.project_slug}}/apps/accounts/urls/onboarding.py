from django.urls import path
from apps.accounts.views.onboarding import OnboardingView

app_name = "accounts_onboarding"

urlpatterns = [
    path("", OnboardingView.as_view(), name="onboarding"),
]
