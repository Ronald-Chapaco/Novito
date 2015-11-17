from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('novo.apps.prod.views',
    url(r'^addProducto/$', 'addProduct_view', name='addProducto'),
    url(r'^edit/producto/(?P<id_prod>.*)/$', 'editProduct_view', name='editProducto'),
    url(r'^productos/page/(?P<pagina>.*)/$', 'producto_view' ,name='productos'),
    url(r'^producto/(?P<id_prod>.*)/$', 'singleProduct_view', name='singleProducto'),
)

