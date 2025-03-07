from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserNotification, GeneralNotification

@login_required
def get_notifications(request):
    """ Fetch both user-specific and general unread notifications """
    user_notifications = UserNotification.objects.filter(user=request.user, is_read=False)
    general_notifications = GeneralNotification.objects.exclude(is_read_by=request.user)

    data = []

    # Add user-specific notifications
    for n in user_notifications:
        data.append({
            "id": n.id, "message": n.message, "link": n.link or "#",
            "type": "personal", "created_at": n.created_at.strftime("%Y-%m-%d %H:%M")
        })

    # Add general notifications
    for n in general_notifications:
        data.append({
            "id": n.id, "message": n.message, "link": n.link or "#",
            "type": "general", "created_at": n.created_at.strftime("%Y-%m-%d %H:%M")
        })

    return JsonResponse({"notifications": data, "count": len(data)})

@login_required
def mark_as_read(request, notification_id, notification_type):
    """ Mark notifications as read when clicked """
    if notification_type == "personal":
        UserNotification.objects.filter(id=notification_id, user=request.user).update(is_read=True)
    elif notification_type == "general":
        general_notification = GeneralNotification.objects.get(id=notification_id)
        general_notification.is_read_by.add(request.user)
        general_notification.save()
    
    return JsonResponse({"status": "success"})
