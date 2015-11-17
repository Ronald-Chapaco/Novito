from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import addProductoForm
from .models import Productos

from django.core.mail import EmailMultiAlternatives #enviamos html
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
import json

#paginacion
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.

# Create your views here.

def addProduct_view(request):
    info = "iniciaco"
    if request.method =="POST":
        form = addProductoForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.status = True
            add.save()  #guardamos la informacion
            form.save_m2m()  #guardar las relaciones many to many
            info = "Guardado satisfactoriamente"
            return HttpResponseRedirect('/productos/producto/%s'%add.id)
    else:
        form = addProductoForm()
    ctx = {'form':form,'informacion':info}
    return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))

def editProduct_view(request,id_prod):
    info = "Iniciado"
    prod = Productos.objects.get(id=id_prod)
    if request.method == "POST":
        form = addProductoForm(request.POST,request.FILES,instance=prod)
        if form.is_valid():
            edit_prod =  form.save(commit=False)
            form.save_m2m()
            edit_prod.status = True
            edit_prod.save()
            info = "Guardado satisfactoriamente"
            return HttpResponseRedirect('/producto/%s/'%edit_prod.id)
    else:
        form = addProductoForm(instance=prod)
    ctx = {'form':form,'informacion':info}
    return render_to_response('ventas/editProducto.html',ctx,context_instance=RequestContext(request))




def producto_view(request,pagina):
    if request.method == "POST":
        if "product_id" in request.POST:
            try:
                id_producto = request.POST['product_id']
                p = Productos.objects.get(pk=id_producto)
                mensaje = {"status":True,"product_id":p.id}
                p.delete()
                print("json 1: %s"%json.dumps(mensaje))
                return HttpResponse(json.dumps(mensaje),mimetype='application/json')
            except:
                mensaje = {'status':False}
                print("json 2: %s"%json.dumps(mensaje))
                return HttpResponse(json.dumps(mensaje),mimetype='application/json')


    lista_prod = Productos.objects.filter(status=True)
    paginator = Paginator(lista_prod,5) # 3= productos por pagina
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        productos = paginator.page(page)
    except(EmptyPage, InvalidPage):
        productos = paginator.page(paginator.num_pages)
    ctx = {'productos':productos}
    return render_to_response('ventas/productos.html',ctx,context_instance=RequestContext(request))



def singleProduct_view(request,id_prod):
    prod = Productos.objects.get(id=id_prod)
    cats = prod.categoria.all()#categorias de producto
    ctx = {'producto':prod,'categoria':cats}
    return render_to_response('ventas/singleProduct.html',ctx,context_instance=RequestContext(request))

