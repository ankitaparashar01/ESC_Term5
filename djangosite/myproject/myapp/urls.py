from django.urls import path, include, re_path
from . import views
# from .views import *

urlpatterns = [
    # Landing page
    path('', views.ascenda, name="ascenda"),
    # path('', views.featureOne, name="ascenda"),
    
    # Confirmation page
    path('confirmation/dest_id=<str:destId>/hotelName=<str:hotelName>/hotelId=<str:hotelId>/roomKey=<str:roomKey>/roomType=<str:roomType>/checkin=<str:checkin>/checkout=<str:checkout>/guests=<str:guests>', views.confirmation, name="confirmation"),
    
    # Transaction complete
    path('transaction-complete/', views.transactionComplete, name="transaction-complete"),
    
    # Hotel cards
    path('hotellistings/', views.hotelCards, name="hotel-cards"),
    
    # Rooms
    path('hotellistings/dest_id=<str:destId>/hotelName=<str:hotelName>/hotelId=<str:hotelId>/checkin=<str:checkin>/checkout=<str:checkout>/guests=<str:guests>', views.RoomList, name="room-list-test-api"), #temporary, will be deleted after transition is settled

     # trying out new url for the form submission temporary
    path('submitmyform', views.submitmyform, name='submitmyform'),
    # path('myform2', views.myform2, name='myform2')

]
