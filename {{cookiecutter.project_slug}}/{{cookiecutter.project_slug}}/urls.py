from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth + MFA
    path("accounts/", include("allauth.urls")),
    path("accounts/two-factor/", include("allauth.mfa.urls")),

    # Onboarding
    path("onboarding/", include("apps.accounts.urls.onboarding", namespace="accounts_onboarding")),

    # Profile
    path("profile/", include("apps.accounts.urls.profile", namespace="accounts_profile")),

    # Sessions
    path("my-sessions/", include("apps.accounts.urls.sessions", namespace="accounts_sessions")),
]
