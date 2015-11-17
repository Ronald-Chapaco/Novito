from django import forms
from .models import Productos

class addProductoForm(forms.ModelForm):
    class Meta:
        model   = Productos
        exclude = {'status',}