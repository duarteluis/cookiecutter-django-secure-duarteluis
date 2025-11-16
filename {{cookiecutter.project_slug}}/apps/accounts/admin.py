from django.contrib import admin
from django.contrib.auth import get_user_model
from user_sessions.models import Session

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_active")

@admin.register(Session)
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ("user", "session_key", "ip", "user_agent", "last_activity")
