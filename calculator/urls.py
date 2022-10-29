
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('depart', views.depart, name="form"),

    path('sh3', views.sh3,name="sh3"),
    path('port', views.port,name="port"),

    path('it2yr', views.it2yr,name="it2yr"),
    path('it2yr3', views.it2yr3,name="it2yr3"),
    path('it2yr4', views.it2yr4,name="it2yr4"),
    path('it2ndyr3R', views.it2ndyr3R,name="it2ndyr3R"),
    path('it2ndyr4R', views.it2ndyr4R,name="it2ndyr4R"),

    path('it3yr', views.it3yr,name="it3yr"),
    path('it3yr5', views.it3yr5,name="it3yr5"),
    path('it3yr6', views.it3yr6,name="it3yr6"),
    path('it3rdyr5R', views.it3rdyr5R,name="it3rdyr5R"),
    path('it3rdyr6R', views.it3rdyr6R,name="it3rdyr6R"),
    
    path('it4yr', views.it4yr,name="it4yr"),
    path('it4yr7', views.it4yr7,name="it4yr7"),
    path('it4yr8', views.it4yr8,name="it4yr8"),
    path('it4yr7R', views.it4yr7R,name="it4yr7R"),
    path('it4yr8R', views.it4yr8R,name="it4yr8R"),

    path('cse', views.cse,name="cse"),
    path('cse2yr', views.cse2yr,name="cse2yr"),
    path('cse2yr3', views.cse2yr3,name="cse2yr3"),
    path('cse2yr4', views.cse2yr4,name="cse2yr4"),
    path('cse3yr', views.cse3yr,name="cse3yr"),
    path('cse3yr5', views.cse3yr5,name="cse3yr5"),
    path('cse3yr5R', views.cse3yr5R,name="cse3yr5R"),
    path('cse3yr6R', views.cse3yr6R,name="cse3yr6R"),
    path('cse4yr', views.cse4yr,name="cse4yr"),
    path('cse4yr7', views.cse4yr7,name="cse4yr7"),
    path('cse4yr8', views.cse4yr8,name="cse4yr8"),
    path('cse4yr7R', views.cse4yr7R,name="cse4yr7R"),


    path('ece', views.ece,name="ece"),
    path('ece2yr', views.ece2yr,name="ece2yr"),
    path('ece2yr3', views.ece2yr3,name="ece2yr3"),
    path('ece2yr3R', views.ece2yr3R,name="ece2yr3R"),
    path('ece2yr4', views.ece2yr4,name="ece2yr4"),
    path('ece2yr4R', views.ece2yr4R,name="ece2yr4R"),
    path('ece3yr', views.ece3yr,name="ece3yr"),
    path('ece3yr5', views.ece3yr5,name="ece3yr5"),
    path('ece3yr5R', views.ece3yr5R,name="ece3yr5R"),
    path('ece3yr6', views.ece3yr6,name="ece3yr6"),


    path('eee', views.eee,name="eee"),
    path('eee2yr', views.eee2yr,name="eee2yr"),
    path('eee2yr3', views.eee2yr3,name="eee2yr3"),
    path('eee2yr4', views.eee2yr4,name="eee2yr4"),
    path('eee3yr', views.eee3yr,name="eee3yr"),
    path('eee3yr5', views.eee3yr5,name="eee3yr5"),
    path('eee3yr6', views.eee3yr6,name="eee3yr6"),


    path('mech', views.mech,name="mech"),
    path('mech2yr', views.mech2yr,name="mech2yr"),
    path('mech2yr3', views.mech2yr3,name="mech2yr3"),
    path('mechR1', views.mechR1,name="mechR1"),
    path('mechR2', views.mechR2,name="mechR2"),
    path('mech2yr4', views.mech2yr4,name="mech2yr4"),
    path('mech3yr', views.mech3yr,name="mech3yr"),
    path('mech3yr5', views.mech3yr5,name="mech3yr5"),
    path('mech3yr6', views.mech3yr6,name="mech3yr6"),


    path('cal', views.cal,name="cal"),
    
    


    
]
