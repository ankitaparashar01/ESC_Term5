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
    

    # location = models.CharField(max_length=200, null=True)
    # price = models.FloatField() #should give cheapest room
    # # hotel website link

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'listingsAndReviews'
