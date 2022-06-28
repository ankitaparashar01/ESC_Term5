from django.urls import path, include, re_path
from . import views
# from .views import *

urlpatterns = [
    path('', views.myfunctioncall, name="index"),
    path('about', views.myfunctionabout, name="about"),
    path('intro/<str:name>/<int:age>', views.intro, name="intro"),
    path('myfirstpage', views.myfirstpage, name="myfirstpage")
]