from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        subject = render_to_string(
            f"account/email/{template_prefix}_subject.txt", context
        ).strip()

        body_txt = render_to_string(
            f"account/email/{template_prefix}.txt", context
        )

        try:
            body_html = render_to_string(
                f"account/email/{template_prefix}.html", context
            )
        except Exception:
            body_html = None

        msg = EmailMultiAlternatives(subject, body_txt,
            settings.DEFAULT_FROM_EMAIL, [email])

        if body_html:
            msg.attach_alternative(body_html, "text/html")

        msg.send()

    def get_login_redirect_url(self, request):
        user = request.user
        if hasattr(user, "onboarding_completed") and not user.onboarding_completed:
            return settings.ONBOARDING_URL
        return settings.LOGIN_REDIRECT_URL
