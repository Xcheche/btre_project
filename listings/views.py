from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Listing
from .choices import bedroom_choices, price_choices, state_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    context = {"listings": paged_listings}

    return render(request, "listings/listings.html", {"listings": paged_listings})


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing": listing}
    return render(request, "listings/listing.html", context)


def search(request):
    context = {
 "bedroom_choices": bedroom_choices,
 "price_choices": price_choices,
 "state_choices": state_choices,

    }
    return render(request, "listings/search.html", context)
