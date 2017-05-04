from django.shortcuts import HttpResponse
from Transport.models import *
import pyrebase
config = {
    "apiKey": "AIzaSyAQHHnCqr-3FajALfmpg19PS44fsB6XkBA",
    "authDomain": "itsystems-162415.firebaseapp.com",
    "databaseURL": "https://itsystems-162415.firebaseio.com",
    "storageBucket" : "itsystems-162415.appspot.com"
  };
firebase = pyrebase.initialize_app(config);
#auth = firebase.auth()
db = firebase.database()
#user = auth.sign_in_with_email_and_password("","")
def index(request,vehi,lat,lon,status):
    coord_l = db.child("My_user").child("Driver").child(vehi).child("Coordinates").get()
    if status == 'false' :
        try :
            lat = float(lat)
            lon = float(lon)
            if (lat/1000 != 1.0 and lon/1000 != 1.0):
                if coord_l.each() == None :
                    coord_l = db.child("My_user").child("Driver").child(vehi).child("Coordinates").get()
            
                coord_list = [p.val() for p in coord_l.each()]

                db.child("My_user").child("Driver").child(vehi).child("Coordinates").update({"P1":"None"})
            
            
                db.child("My_user").child("Driver").child(vehi).update({"latitude":lat, "longitude":lon})
                return HttpResponse("<h3>"+vehi+" @</br>lat: "+str(lat)+"</br>lon: "+str(lon)+"</h3>")
            else :
                return HttpResponse("<h3>The given lat/lon are inappropriate (1000's)...</h3>")
        except:
            return HttpResponse("The given Reg-Number DoesNotExist...")
    

    elif status == 'true' :
        try :
            lat = float(lat)
            lon = float(lon)
            if (lat/1000 != 1.0 and lon/1000 != 1.0):

                if coord_l.each() == None :
                    coord_l = db.child("My_user").child("Driver").child(vehi).child("Coordinates").get()
            
                coord_list = [p.val() for p in coord_l.each()]

                if (coord_list[0] == 'None'):
                    new_latlon = str(lat)+','+str(lon)
                else :
                    new_latlon = str(coord_list[0]) + '|' + str(lat)+','+str(lon)
                
                db.child("My_user").child("Driver").child(vehi).child("Coordinates").update({'P1': new_latlon})

                        
                db.child("My_user").child("Driver").child(vehi).update({"latitude":lat, "longitude":lon})
                return HttpResponse("<h3>"+vehi+" @</br>lat: "+str(lat)+"</br>lon: "+str(lon)+"</h3>"+"\nStatus: "+status)
            else :
                return HttpResponse("<h3>The given lat/lon are inappropriate (1000's)...</h3>")

        except : 
            return HttpResponse("Don't you know the workflow.")
