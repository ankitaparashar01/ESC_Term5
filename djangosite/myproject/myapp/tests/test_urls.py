from django.test import SimpleTestCase
from django.urls import *
from myapp.views import *

class TestUrls(SimpleTestCase):
    def test_ascenda_url_is_resolved(self):
        url = reverse('ascenda')
        self.assertEquals(resolve(url).func, ascenda)

    def test_listings_url_is_resolved(self):
        url = reverse('test-api', args=['destId-str'])
        self.assertEquals(resolve(url).func, testapi)

    def test_roomlist_url_is_resolved(self):
        url = reverse('room-list-test-api', args=['destId-str', 'hotelName-str', 'hotelId-str'])
        self.assertEquals(resolve(url).func, testapiRoomList)

    def test_confirmation_url_is_resolved(self):
        url = reverse('confirmation', args=['destId-str', 'hotelName-str', 'hotelId-str'])
        self.assertEquals(resolve(url).func, confirmation)

    def test_transaction_url_is_resolved(self):
        url = reverse('transaction-complete')
        self.assertEquals(resolve(url).func, transactionComplete)
        

# urlpatterns = [
#     path('', views.ascenda, name="ascenda"),
#     path('hotellist/', views.all_listings, name="list-hotels"), # NOT IN USE
#     path("roomtype/<str:hotelname>", views.roomListPage, name='list-room-type'), # NOT IN USE

#     # TO ADD: confirmation page should have specific room id
#     path('confirmation/dest_id=<str:destId>/name:<str:hotelName>/id=<str:hotelId>', views.confirmation, name="confirmation"),
#     path('transaction-complete/', views.transactionComplete, name="transaction-complete"),

#     #temporary paths below for database transition:
#     path('hotellistings/dest_id=<str:destId>', views.testapi, name="test-api"), #temporary, will be deleted after transition is settled
#     path('hotellistings/dest_id=<str:destId>/name:<str:hotelName>/id=<str:hotelId>', views.testapiRoomList, name="room-list-test-api"), #temporary, will be deleted after transition is settled
#     # path('testapi/name:<str:hotelName>/id=<str:hotelId>', views.testapiRoomList, name="room-list-test-api"), #temporary, will be deleted after transition is settled

# ]
