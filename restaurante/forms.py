from django import forms
from .models import Plato
from django.forms.widgets import PasswordInput, TextInput

class PlatoForm(forms.ModelForm):

    class Meta:
        model = Plato
        fields = ('nombre', 'estado')
        widgets = {
        	'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba El Primer Nombre Del plato'}),
 			'estado': forms.Select(attrs={'class': 'form-control custom-select-value'}),
        }
