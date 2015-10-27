# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from novo.apps.perfil.forms import SignUpForm
from django.contrib.auth.models import User
from novo.apps.feeds.models import Feed

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView, View

from django.core.mail import EmailMultiAlternatives
import random, string
from django.contrib.auth.models import User

class ErrorActiveView(TemplateView):
    template_name = 'auth/error_activacion.html'
    
class UserActiveErrorView(TemplateView):
    template_name = 'auth/usuario_ya_activo.html'

class UserActiveView(TemplateView):
    #model = PerfilOrg
    #fields = ['logo', 'titulo', 'nit', 'fecha_fun', 'direccion', 'tipo', 'obj_actividad', 'acronimo', 'email', 'fax', 'telefono', 'user']
    template_name = 'auth/usuario_activo.html'


class UserCreateView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'auth/signup.html'
    
    def form_valid(self, form):
        form.instance.is_active = False
        form.instance.act = ''.join(random.choice(string.ascii_uppercase + string.digits)
                                               for n in range(20))
        usuario = form.cleaned_data.get('email')
        html_content = 'Por favor visite http://127.0.0.1:8000/signup/activar/%s/ para activar su cuenta' \
                       %(form.instance.act)
        msg = EmailMultiAlternatives('Código de Activación',html_content,\
                                     'friends_77_3@hotmail.com',[usuario])
        msg.attach_alternative(html_content,'text/html') # Definimos el contenido como HTML
        msg.send() # Enviamos el correo
        return super(UserCreateView, self).form_valid(form)


class ActivteUserView(View):
    def dispatch(self, *args, **kwargs):
        self.codigo = self.kwargs['codigo']
        return super(ActivteUserView, self).dispatch(*args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        try:
            self.usuario = User.objects.get(act=self.codigo)
            if self.usuario.is_active == False:
                self.usuario.is_active = True
                self.usuario.save()
                return HttpResponseRedirect("/signup/activo_exito/")
            else:
                return HttpResponseRedirect("/signup/activo/")
        except User.DoesNotExist:
            return HttpResponseRedirect('/signup/error_activacion')