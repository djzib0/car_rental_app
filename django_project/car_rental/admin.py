from django.contrib import admin
from .models import Car, Rent, Reservation

# Register your models here.
admin.site.register(Car)
admin.site.register(Rent)
admin.site.register(Reservation)


