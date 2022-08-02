from django.db import models
from mongoengine import Document, fields
from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField



class ListingItem(models.Model):
    name = models.CharField(db_column='name',max_length=200)
    room_type = models.CharField(db_column='room_type',max_length=200)
    price  = models.FloatField(db_column='price')
    summary = models.CharField(db_column='summary',max_length=200)
    
    
# class DestinationCat(models.Model):
#     termalt = models.CharField(db_column='term',max_length=200)
#     uidalt = models.CharField(db_column='uid',max_length=200)
#     latalt = models.FloatField(db_column='lat')
#     lngalt = models.FloatField(db_column='lng')
#     typealt = models.CharField(db_column='type',max_length=200)
#     statealt = models.CharField(db_column='state',max_length=200)
    

class DestinationCat(models.Model):
    term = models.CharField(db_column='term',max_length=200)
    uid = models.CharField(db_column='uid',max_length=200)
    lat = models.FloatField(db_column='lat')
    lng = models.FloatField(db_column='lng')
    type = models.CharField(db_column='type',max_length=200)
    state = models.CharField(db_column='state',max_length=200)

class HotelSearch(models.Model):
    destinationorhotel = models.CharField(max_length=300, blank=True, default="-")
    uid = models.CharField(max_length=250, blank=True)
    calendarCheckin = models.DateField(blank=True)
    calendarCheckout = models.DateField(blank=True)
    roomsnumber = models.PositiveIntegerField(blank=True)
    adultsnumber = models.PositiveIntegerField(blank=True)
    childrennumber = models.PositiveIntegerField(blank=True)

# This is to add destId inputted from user at the landing into the database 
class DestIdChecker(models.Model):
    destIdFromIndex = models.CharField(max_length=200)

# this is different from the class added at the bottom of views.py -> this has a few elements removed
# This class is made only for use to generate the hotelcards
class Api3UseHotelId(models.Model):
    name = models.CharField(max_length=200)
    rating = models.PositiveIntegerField()
    image_details = JSONField()

# class ImageDetailsApi3 (models.Model):
#     # suffix": ".jpg",
#     #     "count": 56,
#     #     "prefix": "https://d2ey9sqrvkqdfs.cloudfront.net/diH7/"
#     suffix = models.CharField(max_length=200)
#     count = models.PositiveIntegerField()
#     prefix = models.CharField(max_length=200)

