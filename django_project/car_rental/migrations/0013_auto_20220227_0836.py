# Generated by Django 2.2.4 on 2022-02-27 07:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental', '0012_auto_20220227_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='car_year',
        ),
        migrations.AddField(
            model_name='reservation',
            name='car_seats',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
