from django.contrib import admin
from shop.models import Customer, Offer, Provider

admin.site.register([Customer, Offer, Provider])