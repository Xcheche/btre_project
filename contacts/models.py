from datetime import datetime
from django.db import models
from django.utils.timezone import now

from listings.models import Listing


# Create your models here.
class Contact(models.Model):
    listing = models.CharField(max_length=200)
    
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=now, )
    user_id = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.name} on {self.email},{self.contact_date}"

