__author__ = 'Ronald'
from django.conf.urls import patterns, include, url
from .views import *
from django.conf import settings


urlpatterns = patterns('',
                       url(r'^BaseGaleria$', BaseGaleria.as_view(), name='base-galeria'),
                       url(r'^Categoria/$', Categoria_Album.as_view(), name='cat-album'),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                       url(r'^Categoria/(?P<pk>\d+)/Detalle/$', Categoria_detalle.as_view(), name='cat-detalle'),
                       url(r'^ListaFotos/$', ListaFotos.as_view(), name='lista-fotos'),
                       url(r'^Foto/(?P<pk>\d+)/Detalle/$', FotoDetalle.as_view(), name='foto-detalle'),
                       url(r'^Actualizar/(?P<pk>\d+)/Foto/$', ActualizarFoto.as_view(), name='actualizar-foto'),
                       url(r'^SubirFoto/$', SubirFoto.as_view(), name='subir-foto'),
                       url(r'^SubirCategoria/$', SubirCategoria.as_view(), name='subir-categoria'),
                       url(r'^Borrar/(?P<pk>\d+)/Foto/$', BorrarFoto.as_view(), name='borrar-foto'),

)