from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'

class SearchHotelForm(forms.ModelForm):
    destination = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Destination or Hotel",
            "class": "form-control"
        }))
    checkin_date = forms.DateField(widget=DateInput(
        attrs={
            "class": "form-control"
        }
    )
        
        # attrs={
        #     "class": "form-control",
        #     "id": "calendarCheckin",
        #     "name": "calendarCheckin"
        # }
        # )
        )

    checkout_date = forms.DateField(widget=DateInput(
        attrs={
            "class": "form-control"
        }
    )
        # attrs={
        #     "class": "form-control",
        #     "id": "calendarCheckin",
        #     "name": "calendarCheckin"
        # }
    )
    rooms = forms.ChoiceField(widget=forms.Select(
        attrs={
            "class": "form-control"
        },
        # attrs={
        #     "class": "form-control",
        #     "id": "roomsnumber",
        #     "name": "roomsnumber"
        # }
        choices=[('1',1),('2',2),('3',3),('4',4),('5',5)]
    ))
    adults = forms.ChoiceField(widget=forms.Select(
        attrs={
            "class": "form-control"
        },
        # attrs={
        #     "class": "form-control",
        #     "id": "roomsnumber",
        #     "name": "roomsnumber"
        # }
        
        choices=[('1',1),('2',2),('3',3),('4',4),('5',5)]
    ))
    children = forms.ChoiceField(widget=forms.Select(
        attrs={
            "class": "form-control"
        },
        choices=[('1',1),('2',2),('3',3),('4',4),('5',5)]
    ))

    class Meta:
        model = ListingItem
        fields = ('destination', 'checkin_date', 'checkout_date', 'rooms', 'adults', 'children')

    def clean(self):
        cleaned_data = super(SearchHotelForm,self).clean()
        checkin_date = cleaned_data.get("checkin_date")
        checkout_date = cleaned_data.get("checkout_date")
        if checkout_date < checkin_date:
            raise forms.ValidationError("End date should be greater than start date.")



