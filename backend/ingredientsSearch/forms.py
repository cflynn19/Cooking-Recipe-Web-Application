from django import forms
from .models import Search


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Search
        fields = ('image',)