from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',

    url(r'^eventos/$', eventos, name='eve'),
    #url(r'^$', 'articles', name='articles'),
    url(r'^nuevo/$', new_evento),
    url(r'^evento/(?P<evento_id>\d+)$', evento),
    url(r'^evento/edit/(?P<evento_id>\d+)$', edit_evento),
    url(r'^evento/delete/(?P<evento_id>\d+)$', delete_evento),
    url(r'^ruedas/$', ruedas, name='rue'),
    url(r'^nueva/$', new_rueda),
    url(r'^rueda/(?P<rueda_id>\d+)$', rueda),
    url(r'^rueda/edit/(?P<rueda_id>\d+)$', edit_rueda),
    url(r'^rueda/delete/(?P<rueda_id>\d+)$', delete_rueda),
)
