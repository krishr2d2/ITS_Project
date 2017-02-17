from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models
from datetime import datetime
#from geoposition.fields import GeopositionField

# Create your models here.

class My_user(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    My_user_gender      = models.CharField(max_length=1, choices=GENDER_CHOICES)
    My_user_name        = models.CharField(max_length=250)
    My_user_phone       = models.IntegerField()
    My_user_addr        = models.CharField(max_length=250)
    My_user_email       = models.CharField(max_length=250)
    My_user_dateOfBirth = models.DateField()#To know the age of user

class Driver(models.Model):#stores all driver details
    Driver_My_user        = models.ForeignKey(My_user,on_delete:CASCADE)#to get all details from My user
    Driver_currentVehicle = models.ForeignKey(vehicle,on_delete:CASCADE)
    Driver_liscence       = models.CharField(max_length=20)
    Driver_longitude      = models.FloatField()#longitude of driver
    Driver_latitude       = models.FloatField()#latitude  of driver
    #driver_currentVehicle gets current detail of vehicle driver

class Passenger(models.Model):#stores all passangers details
    Passenger_My_user   = models.ForeignKey(My_user,on_delete:CASCADE)#to get all details from My user
    Passenger_latitude  = models.FloatField()#current latitude of passenger
    Passenger_longitude = models.FloatField()#current longitude of passenger
    Passenger_active    = models.BooleanField()#

class Valid_stop(self):#This model stores all the valid stops
    Valid_stop_name      = models.CharField(max_length=50)#name of the stops
    Valid_stop_latitude  = models.FloatField()#latitude of valid stops
    Valid_stop_longitude = models.FloatField()#longitude of valid stops

class Booking(models.Model):#Stores all the information about bookings
    Booking_startpoint  = models.ForeignKey(valid_stop,on_delete:CASCADE)#starting point of booking
    Booking_destination = models.ForeignKey(valid_stop,on_delete:CASCADE)#ending point of booking
    Booking_date        = models.DateTimeField(auto_add_now=True)
    Booking_passanger   = models.ForeignKey(My_user, on_delete=models.CASCADE)#passanger
    Booking_vehicle     = models.ForeignKey(vehicle,  on_delete=models.CASCADE)#vehicle booked
    Booking_status      = models.CharField(max_length=50,default='pending')
    #booking_driver      = models.ForeignKey(driver,on_delete=models.CASCADE)#driver of the vehicle at the time of booking

class Vehicle(models.Model):#Stores information about vehicles
    Vehicle_name      = models.CharField(max_length=200)
    Vehicle_latitude  = models.FloatField()#latitude of vehicle
    Vehicle_longitude = models.FloatField()#longitude of vehicle
    Vehicle_owner     = models.ForeignKey(owner,on_delete:CASCADE)#owner of the vehicle
    Vehicle_rc        = models.CharField(max_length=200)#rc of the vehicle
    Vehicle_active    = models.BooleanField(default=False)#status of vehicle