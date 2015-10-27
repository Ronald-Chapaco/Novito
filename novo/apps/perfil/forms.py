# -*- coding: UTF-8 -*-
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
import re

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Clave',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Ingrese su clave nuevamente',
        widget=forms.PasswordInput()
    )
    username = forms.CharField(label="Nombre de Usuario")
    email = forms.EmailField(label="Email")
    captcha = ReCaptchaField(attrs={'theme': 'clean'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "captcha")


    def clean_password2(self):
        """
        Revisar que ambas claves dadas coincidan
        """
        if 'password1' in self.cleaned_data:
            password = self.cleaned_data['password1']
            password_che = self.cleaned_data['password2']
            if password == password_che:
                        return password_che
            raise forms.ValidationError('Claves no coinciden.')


        def clean_email(self):
            """
                Validar que la direccion de correos dada sea unica en el proyecto
            """
            if User.objects.filter(email__iexact=self.cleaned_data['email']).count():
                raise forms.ValidationError(u'Esta dirección de correos esta en uso, por favor utilice otra')
            return self.cleaned_data['email']
