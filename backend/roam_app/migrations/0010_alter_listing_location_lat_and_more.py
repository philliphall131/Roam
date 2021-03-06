# Generated by Django 4.0.4 on 2022-05-04 21:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roam_app', '0009_alter_listing_location_lat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='location_lat',
            field=models.DecimalField(decimal_places=10, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(-90, message='Latitude must be between -90 and 90'), django.core.validators.MaxValueValidator(90, message='Latitude must be between -90 and 90')]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='location_lng',
            field=models.DecimalField(decimal_places=10, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(-180, message='Longitiude must be between -180 and 180'), django.core.validators.MaxValueValidator(180, message='Longitiude must be between -180 and 180')]),
        ),
    ]
