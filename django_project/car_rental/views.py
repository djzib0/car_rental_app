from django.shortcuts import render, redirect, reverse
from .forms import ReservationForm
from .models import Car, Reservation, Booking
import datetime

today = datetime.date.today()

# Create your views here.
def index_view(request, *args, **kwargs):
    reservation = Reservation()
    if request.method != 'POST':
        form = ReservationForm()
    else:
        form = ReservationForm(data=request.POST)
        form.reservation_from = today
        if form.is_valid():
            reservation.reservation_from = form.cleaned_data['reservation_from']
            reservation.reservation_to = form.cleaned_data['reservation_to']
            reservation.car_seats = form.cleaned_data['car_seats']
            reservation.car_fuel = form.cleaned_data['car_fuel']
            reservation.car_transmission = form.cleaned_data['car_transmission']
            reservation.save()
            return redirect('car_rental:available_cars', reservation_id=reservation.id)
    template = 'index.html'
    context = {}
    context['form'] = form
    return render(request, template, context)


def available_cars_view(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    cars = Car.objects.all()
    bookings = Booking.objects.all()
    available_cars = []
    not_available_cars = []
    rental_days_amount = (reservation.reservation_to - reservation.reservation_from).days
    for booking in bookings:
        if booking.booking_from <= reservation.reservation_from <= booking.booking_to or \
                booking.booking_from <= reservation.reservation_to <= booking.booking_to:
            if booking.booked_car.id not in not_available_cars:
                not_available_cars.append(booking.booked_car.id)
    for car in cars:
        if car.car_seats > reservation.car_seats:
            if car.id not in not_available_cars:
                not_available_cars.append(car.id)
        elif car.car_transmission != reservation.car_transmission:
            if car.id not in not_available_cars:
                not_available_cars.append(car.id)
        elif car.car_fuel != reservation.car_fuel:
            if car.id not in not_available_cars:
                not_available_cars.append(car.id)

    for car in cars:
        if car.id not in not_available_cars:
            available_cars.append(car)

    print(available_cars)
    print(not_available_cars)

    template = 'available_cars.html'
    context = {}
    start_date = str(reservation.reservation_from)
    end_date = str(reservation.reservation_to)

    try:
        # create sessions for start and end date of reservation
        request.session['start_date'] = start_date
        request.session['end_date'] = end_date
        request.session['rental_days_amount'] = rental_days_amount
        request.session['reservation_id'] = reservation.id

        context['available_cars'] = available_cars
        context['bookings'] = bookings
        context['reservation'] = reservation
        return render(request, template, context)
    except:
        return redirect('car_rental:index')



def car_detail(request, car_id):
    try:
        template = 'car_detail.html'
        car = Car.objects.get(id=car_id)

        request.session['car_id'] = car.id

        start_date = request.session['start_date']
        end_date = request.session['end_date']
        reservation_id = request.session['reservation_id']
        car_id = request.session['car_id']
        print(f'this is car id {car_id}')
        context = {}
        context['car'] = car
        context['start_date'] = start_date
        context['end_date'] = end_date
        context['reservation_id'] = reservation_id
        context['car_id'] = car_id
        return render(request, template, context)
    except:
        return redirect('car_rental:index')


def booking_view(request):
    try:
        start_date = request.session['start_date']
        end_date = request.session['end_date']
        car_id = request.session['car_id']
        car = Car.objects.get(id=car_id)
        rental_days_amount = request.session['rental_days_amount']
        rental_days_amount = int(rental_days_amount) * car.car_price_per_day
        # bookings = Booking.objects.all()
        booking = Booking()
        booking.booking_from = start_date
        booking.booking_to = end_date
        booking.booked_car = car
        booking.save()
        template = 'booking.html'
        context = {}
        context['start_date'] = start_date
        context['end_date'] = end_date
        context['car'] = car
        context['booking'] = booking
        context['rental_days_amount'] = rental_days_amount
        del request.session['start_date']
        del request.session['end_date']
        del request.session['car_id']
        return render(request, template, context)

    except:
        template = 'empty.html'
        context = {}
        return render(request, template, context)
