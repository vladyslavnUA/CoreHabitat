from django import forms
from .models import PropertyItem


class PropertyItemForm(forms.ModelForm):
    '''A form to handle creating and updating PropertyItems.'''
    class Meta:
        model = Code
        exclude = [
            'slug',
            'date_posted',
            'last_revised',
            'posted_by',
        ]