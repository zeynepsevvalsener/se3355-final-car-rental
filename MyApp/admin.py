from django.contrib import admin
from .models import Car, Office, Order, Contact, UserProfile

admin.site.register(Car)
admin.site.register(Office)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(UserProfile)

admin.site.site_header = "Car Rental Admin"
admin.site.site_title = "Car Rental Admin Portal"
admin.site.index_title = "Welcome to Car Rental Admin Portal"
