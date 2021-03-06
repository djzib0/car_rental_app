from django.db import models

# importing validator to set min and max value of seat in a car
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Car(models.Model):
    # USUNĄĆ SEATS chyba, że się przyda
    SEATS = [
        ('TWO', '2'),
        ('THR', '3'),
        ('FOU', '4'),
        ('FIV', '5'),
        ('SEV', '7'),
        ('EIG', '8'),
    ]

    TRANSMISSION = [
        ('AUT', 'Automatyczna'),
        ('MAN', 'Manualna'),
    ]

    FUEL = [
        ('GAS', 'Benzyna'),
        ('DIE', 'Diesel'),
        ('LPG', 'LPG'),
        ('ELE', 'Elektryczny'),
        ('HYB', 'Hybryda'),
    ]

    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    car_registration_number = models.CharField(max_length=10, default='XX 1234')
    car_seats = models.PositiveIntegerField(default=5,
                                            validators=[
                                                MaxValueValidator(9),
                                                MinValueValidator(1)
                                            ]
                                            )
    car_year = models.PositiveIntegerField(default=2010)
    car_transmission = models.CharField(max_length=10, choices=TRANSMISSION, default='MAN')
    car_fuel = models.CharField(max_length=10, choices=FUEL, default='GAS')
    car_price_per_day = models.DecimalField(max_digits=6, decimal_places=2, default=150.01)

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'

    def __str__(self):
        return f'{self.car_brand} {self.car_model}'


class Reservation(models.Model):
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
        ('DIE', 'Diesel'),
        ('LPG', 'LPG'),
        ('ELE', 'Elektryczny'),
        ('HYB', 'Hybryda'),
    ]

    reservation_from = models.DateField(verbose_name='OD')
    reservation_to = models.DateField(verbose_name='DO')

    car_seats = models.PositiveIntegerField(default=1,
                                            validators=[
                                                MaxValueValidator(5),
                                                MinValueValidator(1)
                                            ]
                                            )
    car_transmission = models.CharField(max_length=10, choices=TRANSMISSION, default='MAN')
    car_fuel = models.CharField(max_length=10, choices=FUEL, default='GAS')

    def __str__(self):
        return f'Rezerwacja nr: {self.id}'

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'


class Booking(models.Model):
    booked_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    # dodać booked_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_from = models.DateField()
    booking_to = models.DateField()

    def __str__(self):
        return f'Zamówienie nr: {self.id}'

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'


# # Niepotrzebny? wyrzucić
# class Rent(models.Model):
#     rented_car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     rent_start_date = models.DateField(null=True, blank=True)
#     rent_end_date = models.DateField(null=True, blank=True)
#
#
