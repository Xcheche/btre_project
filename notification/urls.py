from django.urls import path
from .views import get_notifications, mark_as_read

urlpatterns = [
    path("get-notifications/", get_notifications, name="get-notifications"),
    path("mark-as-read/<int:notification_id>/", mark_as_read, name="mark-as-read"),
]
