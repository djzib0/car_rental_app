from django.urls import path
from . import views


app_name = 'car_rental'

urlpatterns= [
    path('', views.index_view, name='index'),
    path('car_detail/<int:car_id>', views.car_detail, name='car_detail'),
    path('available_cars/<int:reservation_id>', views.available_cars_view, name='available_cars'),
    path('booking/', views.booking_view, name='booking_view')
]