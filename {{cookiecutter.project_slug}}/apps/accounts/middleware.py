from django.conf import settings
from django.shortcuts import redirect
from allauth.mfa.adapter import get_adapter

class ForceMFAMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.force_mfa = getattr(settings, "FORCE_MFA", False)
        self.setup_url = settings.FORCE_MFA_SETUP_URL
        self.exempt_prefixes = (
            self.setup_url,
            "/onboarding/",
            "/accounts/logout",
            "/admin/",
            "/static/",
            "/media/",
        )

    def __call__(self, request):
        if (
            self.force_mfa
            and request.user.is_authenticated
            and not self._is_exempt(request.path)
        ):
            adapter = get_adapter()
            if not adapter.is_mfa_enabled(request.user):
                return redirect(self.setup_url)

        return self.get_response(request)

    def _is_exempt(self, path):
        return any(path.startswith(p) for p in self.exempt_prefixes)
