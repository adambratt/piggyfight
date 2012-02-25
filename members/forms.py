from django import forms
from images.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        exclude=('name','album', 'member')