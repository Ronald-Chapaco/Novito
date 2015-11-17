# -*- coding: utf-8 -*-
from django import forms
from .models import *

class EventoForm(forms.ModelForm):

    class Meta():
        model = Evento
        fields = (
            'nombre',
            'tipo',
            'fecha_inicio',
            'fecha_fin',
            'localizacion',
            'descripcion',
            'invitados',
            'imagen',
            )
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={
                'class': 'evento-date-form-field field-evento-new'}),
            'fecha_fin': forms.DateInput(attrs={
                'class': 'evento-date-form-field field-evento-new'}),
            'descripcion': forms.Textarea(attrs={
                'class': 'evento-date-form-field field-evento-new'}),
        }



class RuedaForm(forms.ModelForm):

    class Meta():
        model = Rueda
        fields = (
            'titulo',
            'tipo',
            'fecha_inicio',
            'fecha_fin',
            'descripcion',
            'lugar',
            'precio',
            'contacto',
            'imagen',
        )
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={
                'class': 'evento-date-form-field field-evento-new'}),

            'fecha_fin': forms.DateInput(attrs={
                'class': 'evento-date-form-field field-evento-new'}),

            'descripcion': forms.Textarea(attrs={
                'class': 'evento-date-form-field field-evento-new'}),
        }




class SearchBox(forms.Form):
    string = forms.CharField(label='',
        initial='Buscar',
        required=False,
        widget=forms.TextInput(attrs={'class': 'header-seach-form-field'}))

    def clean_string(self):
        string = self.cleaned_data['string']
        if string == "":
            raise forms.ValidationError("Debe ingresar una palabra")
        return string

