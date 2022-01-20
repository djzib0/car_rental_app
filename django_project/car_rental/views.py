from django.shortcuts import render, redirect

from .forms import ReservationForm
from .models import Car, Reservation
import datetime
today = datetime.date.today()

# Create your views here.
def index_view(request):
    reservation = Reservation()
    if request.method != 'POST':
        form = ReservationForm()
    else:
        form = ReservationForm(data=request.POST)
        form.reservation_from = today
        if form.is_valid():
            reservation.reservation_from = form.cleaned_data['reservation_from']
            reservation.reservation_to = form.cleaned_data['reservation_to']
            # reservation.save()
            return redirect('car_rental:available_cars')
    template = 'index.html'
    reservation_id = reservation.id
    context = {}
    context['form'] = form
    context['reservation_id'] = reservation_id
    return render(request, template, context)


def available_cars_view(request):
    # today = datetime.date.today()
    cars = Car.objects.all()
    template = 'available_cars.html'
    context = {}
    context['cars'] = cars
    return render(request, template, context)


def car_detail(request, car_id):
    template = 'car_detail.html'
    car = Car.objects.get(id=car_id)
    context = {}
    context['car'] = car
    return render(request, template, context)


def reservation_view(request):
    template = 'reservation'
    cars = Car.objects.all()
    context = {}
    context['cars'] = cars
    return render(request, template, context)
