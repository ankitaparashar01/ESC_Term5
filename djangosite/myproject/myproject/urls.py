"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from myapp import views

# adding urls from the app into the project in the urls.py but in the myproject
urlpatterns = [
    # Landing page
    path('', views.ascenda, name="ascenda"),
    
    # Confirmation page
    path('confirmation/dest_id=<str:destId>/hotelName=<str:hotelName>/hotelId=<str:hotelId>/roomKey=<str:roomKey>/roomType=<str:roomType>/checkin=<str:checkin>/checkout=<str:checkout>/guests=<str:guests>', views.confirmation, name="confirmation"),
    
    # Transaction complete
    path('transaction-complete/', views.transactionComplete, name="transaction-complete"),

    #ajax helper 
    path('ajax/', views.ajax, name="ajax"),
    path('ajax2/', views.ajax2, name="ajax2"),

    #check order
    path('check-order/', views.check, name="check"),

    #display order
    path('display-order/', views.display, name="display"),
    
    # Hotel cards
    path('hotellistings/', views.hotelCards, name="hotel-cards"),
    
    # Rooms
    path('hotellistings/dest_id=<str:destId>/hotelName=<str:hotelName>/hotelId=<str:hotelId>/checkin=<str:checkin>/checkout=<str:checkout>/guests=<str:guests>', views.RoomList, name="room-list-test-api"), #temporary, will be deleted after transition is settled

     # trying out new url for the form submission temporary
    path('submitmyform', views.submitmyform, name='submitmyform')
    # path('myform2', views.myform2, name='myform2')
]
