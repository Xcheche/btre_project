from django.contrib import admin
from .models import UserNotification, GeneralNotification

@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at', 'link')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'message')

@admin.register(GeneralNotification)
class GeneralNotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at', 'link')
    search_fields = ('message',)
