# Generated by Django 2.2.4 on 2022-03-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rental', '0017_auto_20220302_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.FilePathField(default='/img', verbose_name='/img/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='car_fuel',
            field=models.CharField(choices=[('GAS', 'Benzyna'), ('DIE', 'Diesel'), ('LPG', 'LPG'), ('ELE', 'Elektryczny'), ('HYB', 'Hybryda')], default='GAS', max_length=10),
        ),
    ]
