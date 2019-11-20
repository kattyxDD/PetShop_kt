from django import forms
from .models import *

class Productoform(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'animal',
            'producto',
            'precio',
            'persona',
        ]