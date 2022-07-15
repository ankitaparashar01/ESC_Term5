from django.db import models
import email
from mongoengine import Document, fields
from django.db import models
from django.contrib.auth.models import User

class ListingItem(models.Model):
    name = models.CharField(db_column='name',max_length=200)
    room_type = models.CharField(db_column='room_type',max_length=200)
    price  = models.FloatField(db_column='price')
    summary = models.CharField(db_column='summary',max_length=200)
    
class DestinationCat(models.Model):
    term = models.CharField(db_column='term',max_length=200)
    uid = models.CharField(db_column='uid',max_length=200)
    lat = models.FloatField(db_column='lat')
    lng = models.FloatField(db_column='lng')
    type = models.CharField(db_column='type',max_length=200)
    state = models.CharField(db_column='state',max_length=200)
