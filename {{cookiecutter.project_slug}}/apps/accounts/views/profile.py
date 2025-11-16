from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from allauth.mfa.adapter import get_adapter

from apps.accounts.forms import ProfileForm

class ProfileView(LoginRequiredMixin, FormView):
    template_name = "accounts/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("accounts_profile:profile")

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw["instance"] = self.request.user
        return kw

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Profil mis à jour.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        adapter = get_adapter()
        ctx["mfa_enabled"] = adapter.is_mfa_enabled(self.request.user)
        return ctx
