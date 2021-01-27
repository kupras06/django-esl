import datetime
from django import forms


class CreateEventForm(forms.Form):
    """
    docstring
    """

    # eventme = forms.CharField(required=True)
    event_name = forms.CharField(required=True)
    game_name = forms.CharField(required=True)
    registration_starts = forms.DateTimeField(
        required=True, input_formats=['%d/%m/%Y %H:%M'])
    event_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])


class EditUserForm(forms.Form):
    """
    docstring
    """

    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.TextInput()
    city = forms.CharField()
    country = forms.CharField()
    pin_code = forms.CharField()
