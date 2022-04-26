from django import forms
from .models import *
 
class booksForm(forms.ModelForm):
    class Meta:
        model = books
        fields = [
            "title",
            "author",
            "availability"
        ]