# tunr/forms.py
from django import forms
from .models import Decade, Fad


class DecadeForm(forms.ModelForm):

    class Meta:
        model = Decade
        fields = ('name', 'start_year', 'end_year',)
