from django.db import models

# importing validator to set min and max value of seat in a car
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    car_registration_number = models.CharField(max_length=10, default='XX 1234')
    car_seats = models.PositiveIntegerField(default=1,
                                            validators=[
                                                MaxValueValidator(5),
                                                MinValueValidator(1)
                                            ]
                                            )
    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'

    def __str__(self):
        return f'{self.car_brand} {self.car_model}'


class Reservation(models.Model):
    reservation_from = models.DateField(verbose_name='OD')
    reservation_to = models.DateField(verbose_name='DO')

    def __str__(self):
        return f'Rezerwacja nr: {self.id}'

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'





class Rent(models.Model):
    rented_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rent_start_date = models.DateField(null=True, blank=True)
    rent_end_date = models.DateField(null=True, blank=True)


