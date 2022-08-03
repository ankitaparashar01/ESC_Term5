from django.test import SimpleTestCase
from django.urls import resolve, reverse
from myapp.views import *


class TestUrls(SimpleTestCase):

    def test_index_is_resolved(self):
        url = reverse("ascenda")
        print("checking index url")
        self.assertEquals(resolve(url).func, ascenda)

    def test_confirmation_is_resolved(self):
        url = reverse("confirmation", kwargs={'destId':'WD0M','hotelName':'InterContinental%20Singapore','hotelId':'WaXd','roomKey':'er-6A78CCD73161F643C4E177880190E948-A75724398A23F8B8E49AB02CAC78566E','roomType':'202172293','checkin':'2022-08-20','checkout':'2022-08-22','guests':'2'})
        print("checking confirmation url")
        self.assertEquals(resolve(url).func, confirmation)

    def test_transaction_complete_is_resolved(self):
        url = reverse("transaction-complete")
        print("checking transaction-complete url")
        self.assertEquals(resolve(url).func, transactionComplete)

    def test_ajax1_is_resolved(self):
        url = reverse("ajax")
        print("checking helper ajax url")
        self.assertEquals(resolve(url).func, ajax)

    def test_ajax2_is_resolved(self):
        url = reverse("ajax2")
        print("checking helper ajax2 url")
        self.assertEquals(resolve(url).func, ajax2)

    def test_check_order_is_resolved(self):
        url = reverse("check")
        print("checking check order url")
        self.assertEquals(resolve(url).func, check)

    def test_display_order_is_resolved(self):
        url = reverse("display")
        print("checking display order url")
        self.assertEquals(resolve(url).func, display)

    def test_hotel_cards_is_resolved(self):
        url = reverse("hotel-cards")
        print("checking hotel-cards url")
        self.assertEquals(resolve(url).func, hotelCards)

    def test_room_list_is_resolved(self):
        url = reverse("room-list-test-api",kwargs={'destId':'WD0M','hotelName':'InterContinental%20Singapore','hotelId':'WaXd','checkin':'2022-08-20','checkout':'2022-08-22','guests':'2'})
        print("checking room-listing url")
        self.assertEquals(resolve(url).func, RoomList)

    def test_submitform_is_resolved(self):
        url = reverse("submitmyform")
        print("checking submitmyform url")
        self.assertEquals(resolve(url).func, submitmyform)








