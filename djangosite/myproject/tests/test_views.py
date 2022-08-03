from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import *
import json


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
                
    def test_index_GET(self):

        response = self.client.get(reverse('ascenda'))
        print("checking index views")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')

    def test_confirmation_GET(self):

        response = self.client.get(reverse("confirmation", kwargs={'destId':'WD0M','hotelName':'InterContinental%20Singapore','hotelId':'WaXd','roomKey':'er-6A78CCD73161F643C4E177880190E948-A75724398A23F8B8E49AB02CAC78566E','roomType':'202172293','checkin':'2022-08-20','checkout':'2022-08-22','guests':'2'}))
        print("checking confirmation views")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'confirmation.html')

    def test_Roomlist_GET(self):

        response = self.client.get(reverse("room-list-test-api",kwargs={'destId':'WD0M','hotelName':'InterContinental%20Singapore','hotelId':'WaXd','checkin':'2022-08-20','checkout':'2022-08-22','guests':'2'}))
        print("checking roomlist views")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'roomlisttestapi.html')


    def test_check_order_GET(self):

        response = self.client.get(reverse("check"))
        print("checking check-order views")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'checkorder.html')

    def test_ajax2_GET(self):
        data = {'ID':'Vwh0H8lyYbCkETj4HFcH4ci5wViVtJjQIA_XQvVs5Js='}
        response = self.client.get(reverse("ajax2"),data)
        print("checking ajax2 views")
        self.assertEquals(response.status_code, 200)

    def test_ajax_GET(self):
        data = {'HotelName': 'hotelname',
            'Room': 'room',
            'RoomKey': 'roomkey',
            'Guest': 'guest',
            'CheckIn': 'checkin',
            'CheckOut': 'checkout',
            'RoomRate': 'roomrate',
            'Tax': 'tax',
            'Total': 'total',
            'Title': 'title',
            'FirstName': 'firstname',
            'LastName': 'lastname',
            'CountryCode': 'countrycode',
            'PhoneNumber': 'phonenumber', 
            'Message': 'message',
            'CardNumber' : 'cardnumber',
            'NameOnCard': 'name_on_card',
            'ExpireYear': 'expire_year',
            'ExpireMonth': 'expire_month',
            'CVV': 'cvv'}
        response = self.client.get(reverse("ajax"),data)
        print("checking ajax views")
        self.assertEquals(response.status_code, 200)



