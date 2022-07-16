from django.urls import path, include, re_path
from . import views
# from .views import *

urlpatterns = [
    path('', views.ascenda, name="ascenda"),
    path('hotellist/', views.all_listings, name="list-hotels"),
    path("roomtype/<str:hotelname>", views.roomListPage, name='list-room-type'),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('transaction-complete/', views.transactionComplete, name="transaction-complete"),

    #temporary paths below for database transition:
    path('testapi/dest_id=<str:destId>', views.testapi, name="test-api"), #temporary, will be deleted after transition is settled
    path('testapi/dest_id=<str:destId>/name:<str:hotelName>/id=<str:hotelId>', views.testapiRoomList, name="room-list-test-api"), #temporary, will be deleted after transition is settled
    # path('testapi/name:<str:hotelName>/id=<str:hotelId>', views.testapiRoomList, name="room-list-test-api"), #temporary, will be deleted after transition is settled

]
