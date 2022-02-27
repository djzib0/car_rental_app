from django.contrib import admin
from .models import Car, Reservation, Booking

# Register your models here.
admin.site.register(Car)
admin.site.register(Reservation)
admin.site.register(Booking)
