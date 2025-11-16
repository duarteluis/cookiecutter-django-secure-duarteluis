from django.conf import settings
from allauth.mfa.adapter import DefaultMFAAdapter

class ProjectMFAAdapter(DefaultMFAAdapter):
    def get_totp_issuer(self) -> str:
        return getattr(settings, "MFA_TOTP_ISSUER", settings.PROJECT_NAME)

    def get_totp_label(self, user) -> str:
        return user.email or user.get_username()
