from django.urls import path, include, re_path
from . import views
# from .views import *

urlpatterns = [
    path('', views.ascenda, name="ascenda"),
    # path('hotellist/', views.all_listings, name="list-hotels"), # NOT IN USE
    # path("roomtype/<str:hotelname>", views.roomListPage, name='list-room-type'), # NOT IN USE

    # TO ADD: confirmation page should have specific room id
    path('confirmation/dest_id=<str:destId>/hotelName=<str:hotelName>/hotelId=<str:hotelId>/roomKey=<str:roomKey>/roomType=<str:roomType>', views.confirmation, name="confirmation"),
    path('transaction-complete/', views.transactionComplete, name="transaction-complete"),
    
    #temporary paths below for database transition:
    path('hotellistings/dest_id=<str:destId>', views.hotelCards, name="hotel-cards"), #temporary, will be deleted after transition is settled
    path('hotellistings/dest_id=<str:destId>/hotelName=<str:hotelName>/hotelId=<str:hotelId>', views.RoomList, name="room-list-test-api"), #temporary, will be deleted after transition is settled
    # path('testapi/name:<str:hotelName>/id=<str:hotelId>', views.testapiRoomList, name="room-list-test-api"), #temporary, will be deleted after transition is settled

]
