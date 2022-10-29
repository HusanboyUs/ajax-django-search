from django import forms
from .models import Games

class GameEditForms(forms.ModelForm):
    class Meta:
        model=Games
        fields='__all__'