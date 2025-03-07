from django.db import models
from django.contrib.auth.models import User

# 1️⃣ Model for notifications targeted at specific users
class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    link = models.URLField(blank=True, null=True)  # Optional: Redirect link
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To {self.user.username}: {self.message}"

# 2️⃣ Model for general notifications (for all logged-in users)
class GeneralNotification(models.Model):
    message = models.TextField()
    link = models.URLField(blank=True, null=True)  # Optional: Redirect link
    is_read_by = models.ManyToManyField(User, blank=True)  # Track users who have read it
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"General: {self.message}"
