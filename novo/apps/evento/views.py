from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from itertools import chain
from operator import attrgetter
import datetime
from django.contrib.auth.decorators import login_required
from novo.decorators import ajax_required
from .forms import *
from .models import *
#from fanme.support.models import Notificacion

from django.db.models import Q


def eventos(request):
    searchbox = SearchBox()
    try:
        eventos_creados = request.user.eventos_creados.all().order_by(
            'fecha_inicio')
    except Evento.DoesNotExist:
        eventos_creados = []
    try:
        eventos_invitado = request.user.eventos_invitado.all().order_by(
            'fecha_inicio')
        eventos_noleidos = request.user.eventos_invitado.filter(
            estado="noleido")
        for evento in eventos_noleidos:
            evento.estado = "leido"
            evento.save()
    except Evento.DoesNotExist:
        eventos_invitado = []
    temp = RequestContext(request, {'eventos_creados': eventos_creados,
        'eventos_invitado': eventos_invitado, 'form_search': searchbox})
    return render_to_response('evento/eventos.html', temp)


def new_evento(request):
    searchbox = SearchBox()
    if request.method == "POST":
        form = EventoForm(request.POST, request.FILES)
        #list_ids = request.user.followers.values_list('user', flat=True)
        users = User.objects.all()
        form.fields["invitados"].queryset = users
        if form.is_valid():
            evento = form.save(commit=False)
            creador = request.user
            evento.creador = creador
            evento.fecha_creacion = datetime.datetime.now()
            try:
                evento.imagen = request.FILES['imagen']
            except KeyError:
                pass
            evento.save()
            form.save_m2m()
            return HttpResponseRedirect('/social/eventos/')
    else:
        form = EventoForm()
        #list_ids = request.user.followers.values_list('user', flat=True)
        users = User.objects.all()
        form.fields["invitados"].queryset = users
    template_vars = RequestContext(request, {"form": form,
        'form_search': searchbox})
    return render_to_response('social/new_evento.html', template_vars)


def evento(request, evento_id):
    searchbox = SearchBox()
    creador = False
    try:
        evento = Evento.objects.get(id=evento_id)
        if (evento.creador == request.user):
            creador = True
    except Evento.DoesNotExist:
        evento = []
    temp = RequestContext(request, {'form_search': searchbox, 'evento': evento,
        'creador': creador})
    return render_to_response('evento/evento.html', temp)


def edit_evento(request, evento_id):
    searchbox = SearchBox()
    try:
        evento_db = Evento.objects.get(id=evento_id)
        if not (evento_db.creador == request.user):
            return HttpResponseRedirect('/social/eventos/')
    except Evento.DoesNotExist:
        return HttpResponseRedirect('/social/eventos/')
    if request.method == "POST":
        form = EventoForm(request.POST, request.FILES, instance=evento_db)
        #list_ids = request.user.followers.values_list('user', flat=True)
        users = User.objects.all()
        form.fields["invitados"].queryset = users
        if form.is_valid():
            evento = form.save(commit=False)
            try:
                evento.imagen = request.FILES['imagen']
            except KeyError:
                pass
            evento.save()
            form.save_m2m()
            return HttpResponseRedirect('/social/eventos/')
    else:
        form = EventoForm(instance=evento_db)
        #list_ids = request.user.followers.values_list('user', flat=True)
        users = User.objects.all()
        form.fields["invitados"].queryset = users
    template_vars = RequestContext(request, {"form": form, "user": request.user,
        'form_search': searchbox, 'evento': evento_db})
    return render_to_response('social/edit_evento.html', template_vars)


def delete_evento(request, evento_id):
    searchbox = SearchBox()
    try:
        evento_db = Evento.objects.get(id=evento_id)
        if (evento_db.creador == request.user):
            evento_db.delete()
        return HttpResponseRedirect('/social/eventos/')
    except Evento.DoesNotExist:
        return HttpResponseRedirect('/social/eventos/')
    template_vars = RequestContext(request, {
        'form_search': searchbox, 'evento': evento_db})
    return render_to_response('social/edit_evento.html', template_vars)


def commentevento(request):
    try:
        if request.method == 'POST':
            evento_id = request.POST.get('evento')
            evento = Evento.objects.get(pk=evento_id)
            comment = request.POST.get('comment')
            comment = comment.strip()
            if len(comment) > 0:
                evento_comment = EventoComment(user=request.user, evento=evento, comment=comment)
                evento_comment.save()
            html = u''
            for comment in evento.get_comments_evento():
                html = u'{0}{1}'.format(html, render_to_string('evento/partial_evento_comment.html', {'comment': comment}))
            return HttpResponse(html)
        else:
            return HttpResponseBadRequest()
    except Exception, e:
        return HttpResponseBadRequest()




def ruedas(request):
    searchbox = SearchBox()
    try:
        ruedas_creados = request.user.rudas_creados.all().order_by(
            'fecha_inicio')
    except Rueda.DoesNotExist:
        ruedas_creados = []
    temp = RequestContext(request, {'ruedas_creados': ruedas_creados,
        'form_search': searchbox})
    return render_to_response('evento/ruedas.html', temp)


def new_rueda(request):
    searchbox = SearchBox()
    if request.method == "POST":
        form = RuedaForm(request.POST, request.FILES)
        #list_ids = request.user.followers.values_list('user', flat=True)
        if form.is_valid():
            rueda = form.save(commit=False)
            creador = request.user
            rueda.creador = creador
            rueda.fecha_creacion = datetime.datetime.now()
            try:
                rueda.imagen = request.FILES['imagen']
            except KeyError:
                pass
            rueda.save()
            form.save_m2m()
            return HttpResponseRedirect('/social/ruedas/')
    else:
        form = RuedaForm()
        #list_ids = request.user.followers.values_list('user', flat=True)
    template_vars = RequestContext(request, {"form": form,
        'form_search': searchbox})
    return render_to_response('social/new_rueda.html', template_vars)


def rueda(request, rueda_id):
    searchbox = SearchBox()
    creador = False
    try:
        ruda = Rueda.objects.get(id=rueda_id)
        if (ruda.creador == request.user):
            creador = True
    except Rueda.DoesNotExist:
        ruda = []
    temp = RequestContext(request, {'form_search': searchbox, 'ruda': ruda,
        'creador': creador})
    return render_to_response('social/rueda.html', temp)



def edit_rueda(request, rueda_id):
    searchbox = SearchBox()
    try:
        rueda_db = Rueda.objects.get(id=rueda_id)
        if not (rueda_db.creador == request.user):
            return HttpResponseRedirect('/social/ruedas/')
    except Rueda.DoesNotExist:
        return HttpResponseRedirect('/social/ruedas/')
    if request.method == "POST":
        form = RuedaForm(request.POST, request.FILES, instance=rueda_db)
        #list_ids = request.user.followers.values_list('user', flat=True)
        # users = User.objects.all()
        # form.fields["invitados"].queryset = users
        if form.is_valid():
            rueda = form.save(commit=False)
            try:
                rueda.imagen = request.FILES['imagen']
            except KeyError:
                pass
            rueda.save()
            form.save_m2m()
            return HttpResponseRedirect('/social/ruedas/')
    else:
        form = RuedaForm(instance=rueda_db)
        #list_ids = request.user.followers.values_list('user', flat=True)
        # users = User.objects.all()
        # form.fields["invitados"].queryset = users
    template_vars = RequestContext(request, {"form": form, 
        'form_search': searchbox, 'rueda': rueda_db})
    return render_to_response('social/edit_rueda.html', template_vars)


def delete_rueda(request, rueda_id):
    searchbox = SearchBox()
    try:
        rueda_db = Rueda.objects.get(id=rueda_id)
        if (rueda_db.creador == request.user):
            rueda_db.delete()
        return HttpResponseRedirect('/social/ruedas/')
    except Rueda.DoesNotExist:
        return HttpResponseRedirect('/social/ruedas/')
    template_vars = RequestContext(request, {
        'form_search': searchbox, 'rueda': rueda_db})
    return render_to_response('social/edit_rueda.html', template_vars)