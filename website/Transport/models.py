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
    driver_My_user        = models.ForeignKey(My_user,on_delete:CASCADE)#to get all details from My user
    driver_currentVehicle = models.ForeignKey(vehicle,on_delete:CASCADE)
    driver_liscence       = models.CharField(max_length=20)
    driver_longitude      = models.FloatField()#longitude of driver
    driver_latitude       = models.FloatField()#latitude  of driver
    #driver_currentVehicle gets current detail of vehicle driver

class Passenger(models.Model):#stores all passangers details
    passenger_My_user   = models.ForeignKey(My_user,on_delete:CASCADE)#to get all details from My user
    passenger_latitude  = models.FloatField()#current latitude of passenger
    passenger_longitude = models.FloatField()#current longitude of passenger
    passenger_active    = models.BooleanField()#

class Valid_stop(self):#This model stores all the valid stops
    valid_stop_name      = models.CharField(max_length=50)#name of the stops
    valid_stop_latitude  = models.FloatField()#latitude of valid stops
    valid_stop_longitude = models.FloatField()#longitude of valid stops

class Booking(models.Model):#Stores all the information about bookings
    booking_startpoint  = models.ForeignKey(valid_stop,on_delete:CASCADE)#starting point of booking
    booking_destination = models.ForeignKey(valid_stop,on_delete:CASCADE)#ending point of booking
    booking_date        = models.DateTimeField(auto_add_now=True)
    booking_passanger   = models.ForeignKey(My_user, on_delete=models.CASCADE)#passanger
    booking_vehicle     = models.ForeignKey(vehicle,  on_delete=models.CASCADE)#vehicle booked
    booking_status      = models.CharField(max_length=50,default='pending')
    #booking_driver      = models.ForeignKey(driver,on_delete=models.CASCADE)#driver of the vehicle at the time of booking

class Vehicle(models.Model):#Stores information about vehicles
    vehicle_name      = models.CharField(max_length=200)
    vehicle_latitude  = models.FloatField()#latitude of vehicle
    vehicle_longitude = models.FloatField()#longitude of vehicle
    vehicle_owner     = models.ForeignKey(owner,on_delete:CASCADE)#owner of the vehicle
    vehicle_rc        = models.CharField(max_length=200)#rc of the vehicle
    vehicle_active    = models.BooleanField(default=False)#status of vehicle

    

