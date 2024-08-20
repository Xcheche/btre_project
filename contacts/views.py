from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from .models import Contact  # Ensure the Contact model is correctly imported


# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]

        print(listing_id, listing, name, email, phone, message, user_id)

        # Use a different variable name to avoid conflicts
        new_contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )
        try:
            new_contact.save()  # Save the new contact to the database
            messages.success(
                request,
                "Your request has been submitted, a realtor will get back to you soon!",
            )
            return redirect(reverse("listings:listing", args=[listing_id]))
        except Exception as e:
            messages.error(request, "Error sending request")

    return render(request, "listings/listing.html")
