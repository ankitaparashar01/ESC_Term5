from django.test import TestCase, Client
from django.urls import reverse
from myapp.models import *
from myapp.views import *

class TestViews(TestCase):
   
    def setUp(self):
        self.client = Client()
        
        self.testapi_url = reverse('test-api', args=['destId-str'])
        self.testapiRoomList_url = reverse('room-list-test-api', args=['destId-str', 'hotelName-str', 'hotelId-str'])
        self.confirmation_url = reverse('confirmation', args=['destId-str', 'hotelName-str', 'hotelId-str'])
        self.transactioncomplete_url = reverse('transaction-complete')

        self.checkin = "2022-08-20"
        self.checkout = "2022-08-22"
        self.destId = "WD0M" # Singapore, Singapore (SIN-Changi)"
        self.hotelId = "0vcz" # M Hotel Singapore
        self.guests = "2"

    
    # def test_testapi_GET(self):
    #     response = self.client.get(self.testapi_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, '../templates/NEWhotellistings.html')

    # def test_testapiRoomList_GET(self):
    #     response = self.client.get(self.testapiRoomList_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, '../templates/roomlisttestapi.html')

    # def test_confirmtation_GET(self):
    #     response = self.client.get(self.testapiRoomList_url)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, '../templates/roomlisttestapi.html')

    def test_getRoomsHotelInstanceJSON(self):
        JSONStr = str("https://hotelapi.loyalty.dev/api/hotels/0vcz/price?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1") 
        self.assertEquals(getRoomsHotelInstanceJSON(self.hotelId, self.destId, self.checkin, self.checkout, self.guests), JSONStr)

    def test_getHotelPriceJSON(self):
        JSONStr = str("https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1")
        self.assertEquals(getHotelPriceJSON(self.destId, self.checkin, self.checkout, self.guests), JSONStr)
    