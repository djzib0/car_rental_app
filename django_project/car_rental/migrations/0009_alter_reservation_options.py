# Generated by Django 3.2.11 on 2022-01-19 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental', '0008_auto_20220118_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'Reservation', 'verbose_name_plural': 'Reservations'},
        ),
    ]
