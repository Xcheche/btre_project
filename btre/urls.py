"""
URL configuration for btre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# global urls
urlpatterns = [
    path("", include("pages.urls", namespace="pages")),  # for pages app
    path(
        "accounts/", include("accounts.urls", namespace="accounts")
    ),  # for accounts app
    path(
        "listings/", include("listings.urls", namespace="listings")
    ),  # for listings app
    # for contacts app
    path("contacts/", include("contacts.urls")),
    path("admin/", admin.site.urls),  # for django admin
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # for media files

# for debug toolbar

if settings.DEBUG:
    urlpatterns = [
        *urlpatterns,
        path("__debug__/", include("debug_toolbar.urls")),
    ]
