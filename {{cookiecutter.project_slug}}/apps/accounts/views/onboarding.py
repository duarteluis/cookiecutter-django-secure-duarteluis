from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from allauth.mfa.adapter import get_adapter
from django.conf import settings

class OnboardingView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/onboarding.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        adapter = get_adapter()
        ctx["mfa_enabled"] = adapter.is_mfa_enabled(self.request.user)
        ctx["profile_url"] = reverse_lazy("accounts_profile:profile")
        ctx["sessions_url"] = reverse_lazy("accounts_sessions:list")
        ctx["mfa_setup_url"] = settings.FORCE_MFA_SETUP_URL
        return ctx

    def post(self, request, *args, **kwargs):
        user = request.user
        user.onboarding_completed = True
        user.save(update_fields=["onboarding_completed"])
        messages.success(request, "Onboarding terminé.")
        return redirect(self.success_url)
