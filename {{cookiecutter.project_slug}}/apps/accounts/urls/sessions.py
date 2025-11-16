from django.urls import path
from apps.accounts.views.sessions import (
    SessionListView,
    SessionDeleteView,
    SessionDeleteAllOtherView,
    SessionConfirmDeleteView,
)

app_name = "accounts_sessions"

urlpatterns = [
    path("", SessionListView.as_view(), name="list"),
    path("confirm-delete/<uuid:session_key>/", SessionConfirmDeleteView.as_view(), name="confirm_delete"),
    path("delete/<uuid:session_key>/", SessionDeleteView.as_view(), name="delete"),
    path("delete-others/", SessionDeleteAllOtherView.as_view(), name="delete_others"),
]
