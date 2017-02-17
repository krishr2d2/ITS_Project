from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from Transport.models import *
from Transport.forms import *

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'Transport/index.html')
    context = {
        "form": form,
    }
    return render(request, 'Transport/register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'Transport/index.html')
            else:
                return render(request, 'Transport/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'Transport/login.html', {'error_message': 'Invalid login'})
    return render(request, 'Transport/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'Transport/login.html', context)


def index(request):
     if not request.user.is_authenticated():
           return render(request, 'Transport/login.html')
     else:
           return render(request,'Transport/index.html')

def allpassengers(request):                                     #displays all passengers
    passengers = Passenger.objects.all()
    context    = {
        "passengers":passengers,
    }
    return render(request,"Transport/passengers.html",context)

def alldrivers(request):                                        #display all drivers
    drivers = Driver.objects.all()
    count_Drivers = range(1,drivers.count()+1)
    context = {
    "drivers":drivers,
    "count_Drivers" : count_Drivers,
    }
    return render(request, "Transport/drivers.html",context)

def allvehicles(request):                                       #To display all drivers
    vehicles = Vehicle.objects.all()                            #gets all vehicle details
    context  = {                    
        "vehicles":vehicles,
    }
    return render(request,"Transport/vehicles.html",context)


def driver_details(request,name_id):                            #Details of driver with name_id as id
    driver  = Driver.objects.get(id=name_id)
    context = {
    "driver" : driver,
    }
    return render(request,"Transport/driver.html",context)

def vehicle_details(request,name_id):                           #Details of vehicle with id name_id
    vehicle = Vehicle.objects.get(id=name_id)
    context = {
     "vehicle":vehicle,
     }
    return render(request,"Transport/vehicle_details.html",context)

def passenger_details(request,name_id):                         #Details of passenger with id name_id
    passenger = Passenger.objects.get(id=name_id)
    context   = {
        "passenger":passenger
    }
    return render(request,"Transport/passenger_details.html",context)

'''def Booking(request):
    form = BookingForm()
    context = {
    "form": form,
    }
    return render(request,"Transport/Booking.html",context)'''



