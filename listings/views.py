from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from .models import Listing
from .choices import bedroom_choices, price_choices, state_choices

# View to display the list of published listings with pagination
@login_required
def index(request):
    # Get all published listings ordered by the listing date in descending order
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)

    # Paginate the listings, 3 per page
    paginator = Paginator(listings, 2)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    # Context to pass to the template
    context = {"listings": paged_listings}

    # Render the listings page with the paginated listings
    return render(request, "listings/listings.html", context)

# View to display a single listing's details
@login_required
def listing(request, listing_id):
    # Get the listing by ID or return a 404 error if not found
    listing = get_object_or_404(Listing, pk=listing_id)
    
    # Context to pass to the template
    context = {"listing": listing}
    
    # Render the listing detail page
    return render(request, "listings/listing.html", context)

# View to handle the search functionality
@login_required
def search(request):
    # Get all listings
    queryset_list = Listing.objects.all()
    
    # Initialize state variable
    state = None
    
    # Filter by keywords if provided
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Filter by city if provided
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    # Filter by state if provided
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Filter by number of bedrooms if provided
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Filter by price if provided
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # Context to pass to the template
    context = {
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices,
        "listings": queryset_list,
        "values": request.GET,
    }
    
    # Render the search results page
    return render(request, "listings/search.html", context)
