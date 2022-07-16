from django import forms
from .models import *


class DestinationCreationForm(forms.ModelForm):
    class Meta:
        model = DestinationCat
        fields = '__all__'
