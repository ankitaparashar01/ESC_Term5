from django.test import TestCase
from myapp.models import *

class TestModels(TestCase):
    def setUp(self):
        self.DestinationCat = DestinationCat.objects.create(
            term = "Bali, Indonesia",
            uid = "WP3Z",
            lat = -8.409518,
            lng = 115.187989,
            type =  "city"
        )

    def test_airport_or_city(self):
        self.assertEquals(DestinationCat.airport_or_city(self.DestinationCat), True)
        
        destinationCat2 = DestinationCat.objects.create(
            term = "Bali, Indonesia",
            uid = "WP3Z",
            lat = -8.409518,
            lng = 115.187989,
            type =  "notairportorcity"
        )
        self.assertEquals(DestinationCat.airport_or_city(destinationCat2), False)
        


# class DestinationCat(models.Model):
#     term = models.CharField(db_column='term',max_length=200)
#     uid = models.CharField(db_column='uid',max_length=200)
#     lat = models.FloatField(db_column='lat')
#     lng = models.FloatField(db_column='lng')
#     type = models.CharField(db_column='type',max_length=200)
#     state = models.CharField(db_column='state',max_length=200)