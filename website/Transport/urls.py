from django.conf.urls import url
from . import views
from mylogin import views as logviews
app_name = 'Transport'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', logviews.register, name='register'),
    url(r'^login/$', logviews.login_user, name='login_user'),
    url(r'^register/success/$',logviews.register_success),
    url(r'^logout_user/$', logviews.logout_user, name='logout_user'),
<<<<<<< HEAD
    #url(r'^Booking/$',views.Booking,name="Booking"),
    #url(r'^vehicle_details/$',views.vehicle_details,name="vehicle_details"),
    url(r'^driver_accounts/(?P<name_id>[1-6])/$',views.place,name="place"),
    url(r'^user_accounts/',views.user_accounts, name='user_accounts'),
    url(r'^driver_accounts/',views.driver_accounts, name='driver_accounts'),
    url(r'^allvehicles/',views.allvehicles, name='allvehicles'),#URL which shows all drivers
=======

    url(r'^allpassengers/',views.allpassengers, name='allpassengers'),    
    url(r'^alldrivers/',views.alldrivers, name='alldrivers'),
    url(r'^allvehicles/',views.allvehicles,name='allvehicles'),    
    url(r'^passenger_details/(?P<name_id>[1-6])/$',views.passenger_details,name="passenger_details"),
    url(r'^driver_details/(?P<name_id>[1-6])/$',views.driver_details,name="driver_details"),
    url(r'^vehicle_details/(?P<name_id>[1-6])/$',views.vehicle_details,name="vehicle_details"),

>>>>>>> 184665029f4a676d1202a6bbec499b9f20b9173c
]
