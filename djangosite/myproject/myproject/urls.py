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
#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include('myapp.urls'))
#]
urlpatterns = [
    # path('', views.myfunctioncall, name="index"),
    # path('about', views.myfunctionabout, name="about"),
    # path('intro/<str:name>/<int:age>', views.intro, name="intro"),
    path('', views.ascenda, name="ascenda"),
    path('hotellist/', views.all_listings, name="list-hotels"),
    path("roomtype/<str:hotelname>", views.roomListPage, name='list-room-type'),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('transaction-complete/', views.transactionComplete, name="transaction-complete"),
    path('ajax/', views.ajax),
    path('ajax2/', views.ajax2),
    path('check-order/', views.check, name="check"),
    path('display-order/', views.display)
]
