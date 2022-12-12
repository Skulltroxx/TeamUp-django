from django import forms
from .models import Event

class AddForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('sport', 'arena', 'date')

        widgets={
            'date': forms.DateInput(attrs={'type': 'date'})
        }