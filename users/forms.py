from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserProfileForm(UserCreationForm):
    lat = forms.DecimalField(max_digits=9, decimal_places=6)
    long = forms.DecimalField(max_digits=9, decimal_places=6)
    email = forms.EmailField(max_length=75)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('lat', 'long', 'email')
