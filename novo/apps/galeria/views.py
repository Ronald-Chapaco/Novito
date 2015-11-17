from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.

class BaseGaleria(TemplateView):
    template_name = 'BaseGaleria.html'

class Categoria_Album(ListView):
    model = Categoria
    template_name = 'galeria/categoria.html'

class Categoria_detalle(DetailView):
    model = Categoria
    template_name = 'galeria/CategoriaDetalle.html'


class ListaFotos(ListView ):
    model = Fotos
    template_name = 'galeria/ListaFotos.html'


class FotoDetalle(DetailView):
    model = Fotos
    template_name = 'galeria/FotoDetalle.html'

    def get_context_data(self, **kwargs):
        context = super(FotoDetalle, self).get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context

    def post(self, request,  *args, **kwargs):
        id=self.get_object().id
        if(request.method=="POST"):
            comentario=ComentarioForm(request.POST.copy())
            comentario.instance.user = self.request.user
            comentario.instance.foto = self.get_object()
            comentario.data['foto'] = self.get_object().id
            comentario.data['user'] = self.get_object().id
            if(comentario.is_valid()):
                comentario.save()
                return HttpResponseRedirect('/galeria/ListaFotos')

class ActualizarFoto(UpdateView):
    model = Fotos
    fields = ['categoria', 'titulo', 'foto', 'favorito', 'user']
    template_name = 'galeria/SubirActualizarFoto.html'

class SubirFoto(CreateView):
    model = Fotos
    fields = ['categoria', 'titulo', 'foto', 'favorito', 'user']
    template_name = 'galeria/AgregarFoto.html'

class SubirCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'galeria/AgregarCategoria.html'    

class BorrarFoto(DeleteView):
    model = Fotos
    success_url = reverse_lazy('lista-fotos')
    template_name = 'galeria/BorrarFoto.html'