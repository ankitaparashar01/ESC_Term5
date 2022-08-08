from django.test import TestCase
from myapp.models import *

class TestModels(TestCase):
    def setUp(self):
        HotelSearch.objects.bulk_create(
            [HotelSearch(destinationorhotel='InterContinental%20Singapore', uid = '2',calendarCheckin = '2022-08-20',calendarCheckout = '2022-08-22',roomsnumber ='1',adultsnumber='2',childrennumber='1'),
            HotelSearch(destinationorhotel='InterContinental%20Singapore', uid = '2',calendarCheckin = '2022-08-20',calendarCheckout = '2022-08-22',roomsnumber ='2',adultsnumber='2',childrennumber='1'),
            HotelSearch(destinationorhotel='InterContinental%20Singapore', uid = '2',calendarCheckin = '2022-08-20',calendarCheckout = '2022-08-22',roomsnumber ='3',adultsnumber='2',childrennumber='1')]
            )

        ListingItem.objects.create(name = 'a', room_type='single',price = 2022.2, summary="ok")
         
    def test_uid_maxlength(self):
        
        print("checking uid maxlength")
        hotel = HotelSearch.objects.filter(roomsnumber='1').first()
        max_length = hotel._meta.get_field('uid').max_length
        self.assertEquals(max_length,250)
    
    def test_desorhotel_maxlength(self):

        print("checking destinationorhotel maxlength")
        hotel = HotelSearch.objects.filter(roomsnumber='1').first()
        max_length = hotel._meta.get_field('destinationorhotel').max_length
        self.assertEquals(max_length,300)

    def test_uid_lable(self):
        
        print("checking lable")
        hotel = HotelSearch.objects.filter(roomsnumber='3').first()
        field_label = hotel._meta.get_field('uid').verbose_name
        self.assertEquals(field_label,'uid')

    def test_name_max_length(self):
        print("checking ListingItem maxlength")
        item = ListingItem.objects.filter(name ='a').first()
        max_length1 = item._meta.get_field('name').max_length
        max_length2 = item._meta.get_field('room_type').max_length
        max_length3 = item._meta.get_field('summary').max_length
        self.assertEquals(max_length1,200)
        self.assertEquals(max_length2,200)
        self.assertEquals(max_length3,200)

