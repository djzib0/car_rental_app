import datetime

from django import forms
from django.forms import Form, SelectDateWidget
import datetime

from .models import Car, Reservation
from django.contrib.admin.widgets import AdminDateWidget

class ReservationForm(forms.Form):
    TRANSMISSION = [
        ('AUT', 'Automatyczna'),
        ('MAN', 'Manualna'),
    ]

    CATEGORY = [
        ('SMA', 'Mały'),
        ('MED', 'Średni'),
        ('LAR', 'Duży'),
        ('KOM', 'Kombi'),
        ('MIN', 'Minivan'),
        ('SUV', 'SUV'),
    ]

    FUEL = [
        ('GAS', 'Benzyna'),
        ('LPG', 'LPG'),
        ('ELE', 'Elektryczny'),
    ]

    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    model = Reservation
    reservation_from = forms.DateField(widget=forms.SelectDateWidget, initial=today, label='Rezerwacja od:')
    reservation_to = forms.DateField(widget=forms.SelectDateWidget, initial=tomorrow, label='Rezerwacja do:')
    car_seats = forms.IntegerField(min_value=2, max_value=10, label='Ilość miejsc')
    car_transmission = forms.ChoiceField(choices=TRANSMISSION, label='Skrzynia biegów')
    car_fuel = forms.ChoiceField(choices=FUEL, label='Rodzaj paliwa')
    labels = ['text']

    def clean(self):
        today = datetime.date.today()
        cleaned_data = super().clean()
        reservation_from = cleaned_data.get('reservation_from')
        reservation_to = cleaned_data.get('reservation_to')
        if reservation_to <= reservation_from:
            raise  forms.ValidationError("Data końcowa musi być późniejsza niż początkowa.")
        if reservation_from < today:
            raise forms.ValidationError("Ustaw rozpoczęcia od dzisiejszego dnia lub późniejszej daty.")
        if reservation_to <= today:
            raise forms.ValidationError("Data zakończenia najmu musi być późniejsza niż dzisiaj.")
        car_seats = cleaned_data.get('car_seats')
        car_transmission = cleaned_data.get('car_transmission')
        car_fuel = cleaned_data.get('car_fuel')





