from django import forms
from .models import *


class DestinationCreationForm(forms.ModelForm):
    class Meta:
        model = DestinationCat
        fields = '__all__'


# to ankita, you can add the form thingy below here! 
# i will eventually delete DestinationCreationForm but for now im still using it
# :>
