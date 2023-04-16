import datetime

from django import forms
from django.forms import Form, SelectDateWidget
import datetime

from .models import Car, Reservation
from django.contrib.admin.widgets import AdminDateWidget

class ReservationForm(forms.Form):
    TRANSMISSION = [
        ('AUT', 'Automatic'),
        ('MAN', 'Manual'),
    ]

    FUEL = [
        ('GAS', 'Gas'),
        ('DIE', 'Diesel'),
        ('LPG', 'LPG'),
        ('ELE', 'Electric'),
        ('HYB', 'Hybrid'),
    ]

    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    model = Reservation
    reservation_from = forms.DateField(widget=forms.SelectDateWidget, initial=today, label='Reservation from:')
    reservation_to = forms.DateField(widget=forms.SelectDateWidget, initial=tomorrow, label='Reservation to:')
    car_seats = forms.IntegerField(min_value=2, max_value=10, label='Numer of seats')
    car_transmission = forms.ChoiceField(choices=TRANSMISSION, label='Transmission')
    car_fuel = forms.ChoiceField(choices=FUEL, label='Fuel type')
    labels = ['text']

    def clean(self):
        today = datetime.date.today()
        cleaned_data = super().clean()
        reservation_from = cleaned_data.get('reservation_from')
        reservation_to = cleaned_data.get('reservation_to')
        if reservation_to <= reservation_from:
            raise  forms.ValidationError("End date must be greater than start date.")
        if reservation_from < today:
            raise forms.ValidationError("Choose today date or greater.")
        if reservation_to <= today:
            raise forms.ValidationError("End date must be greater than today date.")
        car_seats = cleaned_data.get('car_seats')
        car_transmission = cleaned_data.get('car_transmission')
        car_fuel = cleaned_data.get('car_fuel')

