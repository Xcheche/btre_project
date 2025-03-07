from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags

from btre import settings
from listings.models import Listing
from .models import Contact





def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.user.id if request.user.is_authenticated else 0  # Default to 0
        
        listing = get_object_or_404(Listing, id=listing_id)
        realtor_email = listing.realtor.email

        if Contact.objects.filter(listing_id=listing_id, email=email).exists():
            messages.error(request, "You have already made an inquiry for this listing.")
            return redirect(reverse("listings:listing", args=[listing_id]))

        new_contact = Contact(
            listing=listing.title,  # ✅ Store as string
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )

        try:
            new_contact.save()

            send_mail(
                subject="New Property Inquiry",
                message=f"New inquiry for {listing.title}.\n\nDetails:\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}\n\nSign into the admin panel for more info.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[realtor_email],
                fail_silently=False,
            )

            user_email_template = f"""
            <div style="max-width: 600px; margin: auto; padding: 20px; 
                        font-family: Arial, sans-serif; border: 1px solid #ddd; border-radius: 8px;">
                <h2 class="text-success text-center" style="color: #28a745;">Thank You for Your Inquiry!</h2>
                <p>Dear {name},</p>
                <p>Thank you for inquiring about <strong>{listing.title}</strong>. A realtor will get back to you soon!</p>
                <div style="background-color: #f8f9fa; padding: 15px; border-left: 4px solid #28a745;">
                    <p><strong>Your Message:</strong></p>
                    <p>{message}</p>
                </div>
                <p class="text-center" style="text-align: center;">Best Regards,<br><strong>Your Real Estate Team</strong></p>
            </div>
            """

            user_plain_text = strip_tags(user_email_template)

            email_user = EmailMultiAlternatives(
                subject="Thank You for Your Inquiry",
                body=user_plain_text,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email]
            )
            email_user.attach_alternative(user_email_template, "text/html")
            email_user.send()

            messages.success(request, "Your request has been submitted, a realtor will get back to you soon!")
            return redirect(reverse("listings:listing", args=[listing_id]))

        except Exception as e:
            import traceback
            print(traceback.format_exc())  # Logs full error
            messages.error(request, f"Error sending request: {e}")

    return render(request, "listings/listing.html")
