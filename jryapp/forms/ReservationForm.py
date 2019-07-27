from django import forms
from jryapp.models import Reservation
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ('user','pcroom', 'startDate', 'endDate')