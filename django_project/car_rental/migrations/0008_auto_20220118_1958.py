# Generated by Django 3.2.11 on 2022-01-18 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental', '0007_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_from',
            field=models.DateField(verbose_name='OD'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_to',
            field=models.DateField(verbose_name='DO'),
        ),
    ]
