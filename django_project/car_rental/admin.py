from django.contrib import admin
from .models import Car, Reservation, Booking

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_brand', 'car_model', 'car_registration_number', 'car_year']
    list_filter =['car_brand', 'car_model', 'car_year', 'car_transmission', 'car_fuel']
    search_fields = ['car_brand', 'car_model', 'car_year']


admin.site.register(Car, CarAdmin)
admin.site.register(Reservation)
admin.site.register(Booking)
