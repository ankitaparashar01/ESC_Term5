from django import forms
from .models import *


class DestinationCreationForm(forms.ModelForm):
    class Meta:
        model = DestinationCat
        fields = '__all__'


# to ankita, you can add the form thingy below here! 
# i will eventually delete DestinationCreationForm but for now im still using it
# :>
class SearchHotelForm(forms.ModelForm):
    destination = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Destination or Hotel",
            "class": "form-control"
        }))
    checkin_date = forms.DateField(widget=forms.DateInput(
        attrs={
            "class": "form-control"
        }))

    checkout_date = forms.DateField(widget=forms.DateInput(
        attrs={
            "class": "form-control"
        }
    ))
    rooms = forms.

