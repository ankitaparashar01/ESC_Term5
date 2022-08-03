from django.test import SimpleTestCase

from myapp.checkvalue import *
from myapp.helper import *

# Create your tests here.
#unit testing 1: helper function for the confrimation and transaction page
class TestConfirmationHelper(SimpleTestCase):
    def setUp(self):
        self.title1 = "Mrs. "
        self.title3 = 'Ms'

        self.phonenumber1 = "+6584672105"
        self.phonenumber2 = '+868412'

        self.cvv1 = '888'
        self.cvv2 = 'acv'

        self.cardnumber1 ='4218005468712354'
        self.cardnumber2 ='4218005468712354a'
        self.cardnumber3 ='11111111111111111111111111111111111'

        self.expiry1 = ['2024','2']
        self.expiry2 = ['2022','2']

        self.empty1 = '1'
        self.empty2 = ''

    def test_check_title(self):
        print("Checking title")
        self.assertEqual(check_title(self.title1), True)
        self.assertEqual(check_title(self.title3), False)

    def test_check_phonenumber(self):
        print("Checking phonenumber")
        self.assertEqual(check_phonenumber(self.phonenumber1), True)
        self.assertEqual(check_phonenumber(self.phonenumber2), False)


    def test_check_cvv(self):
        print("Checking cvv")
        self.assertEqual(check_cvv(self.cvv1), True)
        self.assertEqual(check_cvv(self.cvv2), False)

    def test_check_cardnumber(self):
        print("Checking cardnumber")
        self.assertEqual(check_cardnumber(self.cardnumber1), True)
        self.assertEqual(check_cardnumber(self.cardnumber2), False)
        self.assertEqual(check_cardnumber(self.cardnumber3), False)
        
    def test_check_expiry(self):
        print("Checking expiry date")
        self.assertEqual(check_expire(self.expiry1[0],self.expiry1[1]), True)
        self.assertEqual(check_expire(self.expiry2[0],self.expiry2[1]), False)
    
    def test_check_empty(self):
        print("Checking if empty")
        self.assertEqual(check_not_empty(self.empty1), True)
        self.assertEqual(check_not_empty(self.empty2), False)


    def test_API1(self):
        print("checking helper API funtion 1")
        string = getAllHotelsPricesWDest('WD0M', '2022-08-20', '2022-08-22', '2')
        self.assertEqual(string, 'https://hotelapi.loyalty.dev/api/hotels/prices?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1')

    def test_API2(self):
        print("checking helper API funtion 2")
        string = getSingleHotelRoomTypes('WaXd', 'WD0M', '2022-08-20', '2022-08-22', '2')
        self.assertEqual(string, 'https://hotelapi.loyalty.dev/api/hotels/WaXd/price?destination_id=WD0M&checkin=2022-08-20&checkout=2022-08-22&lang=en_US&currency=SGD&country_code=SG&guests=2&partner_id=1')

    def test_API3(self):
        print("checking helper API funtion 3")
        string = getHotelCardWHotelID('WaXd')
        self.assertEqual(string, 'https://hotelapi.loyalty.dev/api/hotels/WaXd')


    def getSingleHotelCardWHotelID(self):
        print("checking helper API funtion 4")
        string = getSingleHotelRoomTypes('WD0M')
        self.assertEqual(string, 'https://hotelapi.loyalty.dev/api/hotels?destination_id=WD0M')

    

