from django.urls import path
from . import views

# Define the application namespace
app_name = "listings"

# URL patterns for the listings app
urlpatterns = [
    # URL pattern for the index view, which displays all listings
    path("", views.index, name="listings"),
    
    # URL pattern for the listing view, which displays a specific listing by its ID
    path("<int:listing_id>/", views.listing, name="listing"),
    
    # URL pattern for the search view, which allows users to search for listings
    path("search/", views.search, name="search"),
]
