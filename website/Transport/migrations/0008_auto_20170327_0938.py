# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-27 04:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Transport', '0007_auto_20170327_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Booking_vehicle',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='Transport.Vehicle'),
        ),
    ]
