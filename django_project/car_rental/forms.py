import datetime

from django import forms
from django.forms import Form, SelectDateWidget
import datetime

from .models import Car, Reservation
from django.contrib.admin.widgets import AdminDateWidget

class ReservationForm(forms.Form):
    today = datetime.date.today()
    model = Reservation
    reservation_from = forms.DateField(widget=forms.SelectDateWidget)
    reservation_to = forms.DateField(widget=forms.SelectDateWidget)
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




