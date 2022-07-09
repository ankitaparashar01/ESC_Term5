from django.urls import path, include, re_path
from . import views
# from .views import *

urlpatterns = [
    # path('', views.myfunctioncall, name="index"),
    # path('about', views.myfunctionabout, name="about"),
    # path('intro/<str:name>/<int:age>', views.intro, name="intro"),
    path('', views.ascenda, name="ascenda"),
    path('hotellist/', views.all_listings, name="list-hotels"),
    path("roomtype/<str:hotelname>", views.roomListPage, name='list-room-type'),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('transaction-complete/', views.transactionComplete, name="transaction-complete")
]