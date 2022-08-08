from django.test import SimpleTestCase
from myapp.forms import *

class TestForm(SimpleTestCase):

    def test_searchhotelform_valid_data(self):
        print("checking forms")
        form = SearchHotelForm(data = {
            'destination':'Singapore',
            'checkin_date':'2022-08-20',
            'checkout_date':'2022-08-22',
            'rooms':'1',
            'adults':'1',
            'children':'1'
        })

        self.assertFalse(form.is_valid())
        

    def test_searchhotelform_valid_data(self):
        form = SearchHotelForm(data = {
            'checkin_date':'2022-08-20',
            'checkout_date':'2022-08-22'

        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)
