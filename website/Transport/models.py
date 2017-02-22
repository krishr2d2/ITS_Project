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
    My_user_gender      = models.CharField(max_length=1, choices=GENDER_CHOICES,default=None)
    My_user_name        = models.CharField(max_length=250,default=None)
    My_user_phone       = models.IntegerField(default=None)
    My_user_addr        = models.CharField(max_length=250,default=None)
    My_user_email       = models.CharField(max_length=250,default=None)
    My_user_dateOfBirth = models.DateField(default=None,null=True)#To know the age of user

class Vehicle(models.Model):#Stores information about vehicles
    Vehicle_name      = models.CharField(max_length=200,default=None)
    Vehicle_latitude  = models.FloatField(default=None)#latitude of vehicle
    Vehicle_longitude = models.FloatField(default=None)#longitude of vehicle
    Vehicle_rc        = models.CharField(max_length=200,default=None)#rc of the vehicle
    Vehicle_active    = models.BooleanField(default=None)#status of vehicle

class Driver(models.Model):#stores all driver details
    Driver_My_user        = models.ForeignKey(My_user,on_delete=models.CASCADE, default=0,blank=True)#to get all details from My user
    Driver_currentVehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE, default=0)
    Driver_liscence       = models.CharField(max_length=20,default=None)
    Driver_longitude      = models.FloatField(default=None)#longitude of driver
    Driver_latitude       = models.FloatField(default=None)#latitude  of driver
    #driver_currentVehicle gets current detail of vehicle driver

class Passenger(models.Model):#stores all passangers details
    Passenger_My_user   = models.ForeignKey(My_user,on_delete=models.CASCADE, default=0)#to get all details from My user
    Passenger_latitude  = models.FloatField(default=None)#current latitude of passenger
    Passenger_longitude = models.FloatField(default=None)#current longitude of passenger
    Passenger_active    = models.BooleanField(default=None)#

class Valid_stop(models.Model):#This model stores all the valid stops
    Valid_stop_name      = models.CharField(max_length=50,default=None)#name of the stops
    Valid_stop_latitude  = models.FloatField(default=None)#latitude of valid stops
    Valid_stop_longitude = models.FloatField(default=None)#longitude of valid stops

class Booking(models.Model):#Stores all the information about bookings
    Booking_startpoint  = models.ForeignKey(Valid_stop,default=0,on_delete=models.CASCADE,related_name='%(class)s_starting_point')#starting point of booking
    Booking_destination = models.ForeignKey(Valid_stop, default=0,on_delete=models.CASCADE,related_name='%(class)s_destination_point')#ending point of booking
    Booking_date        = models.DateTimeField(auto_now_add=True)
    Booking_passenger   = models.ForeignKey(Passenger, default=0,on_delete=models.CASCADE)#passanger
    Booking_vehicle     = models.ForeignKey(Vehicle,default=0,on_delete=models.CASCADE)#vehicle booked
    Booking_status      = models.CharField(max_length=50,default=None)
    #booking_driver      = models.ForeignKey(driver,on_delete=models.CASCADE)#driver of the vehicle at the time of booking

