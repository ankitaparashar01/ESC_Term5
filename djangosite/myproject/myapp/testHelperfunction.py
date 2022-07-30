import unittest
from checkvalue import *


class TestStringMethods(unittest.TestCase):
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



if __name__ == '__main__':
    unittest.main()