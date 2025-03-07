from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import send_mail

from btre import settings
from contacts.models import Contact


# Create your views here.
def register(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        # Check if passwords match
        
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is taken")
                return redirect("accounts:register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is being used")
                    return redirect("accounts:register")
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, "You are now registered and can log in")
                    return redirect("accounts:login")
                send_mail(
                    'Welcome to BTRE RealEstate',
                    'Thank you for registering with BTRE. We are glad to have you!',
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )
        else:
            messages.error(request, "Passwords do not match")
            return redirect("accounts:register")
    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        # login logic
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("accounts:dashboard")

        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You have been logged out")
       
       
    return redirect("accounts:login")



def dashboard(request):
    inquiries = Contact.objects.filter(user_id=request.user.id).order_by("-contact_date")
    print(inquiries) 
    context = {
        "inquiries": inquiries,
    }
    return render(request, "accounts/dashboard.html")
