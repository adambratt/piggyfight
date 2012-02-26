from django import forms
from game.models import MMS


class MMSForm(forms.ModelForm):
    class Meta:
        model=MMS