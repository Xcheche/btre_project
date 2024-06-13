from django.shortcuts import render

from .models import Listing


# Create your views here.
def index(request):
    listings = Listing.objects.all()

    return render(request, "listings/listings.html",{"listings": listings})


def listing(request, listing_id):
    return render(request, "listings/listing.html")


def search(request):
    return render(request, "listings/search.html")
