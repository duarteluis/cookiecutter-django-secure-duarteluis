from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from user_sessions.models import Session
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

class SessionListView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/sessions/list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["sessions"] = Session.objects.filter(user=self.request.user)
        ctx["current_session_key"] = self.request.session.session_key
        return ctx


class SessionDeleteView(LoginRequiredMixin, View):
    def post(self, request, session_key):
        session = get_object_or_404(Session, session_key=session_key, user=request.user)
        session.delete()
        return redirect("accounts_sessions:list")


class SessionDeleteAllOtherView(LoginRequiredMixin, View):
    def post(self, request):
        current_key = request.session.session_key
        Session.objects.filter(user=request.user).exclude(session_key=current_key).delete()
        return redirect("accounts_sessions:list")


class SessionConfirmDeleteView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/sessions/confirm_delete.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        session_key = self.kwargs["session_key"]
        ctx["session"] = get_object_or_404(Session, session_key=session_key, user=self.request.user)
        return ctx