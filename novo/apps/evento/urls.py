from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
    url(r'^eventos/$', eventos, name='eve'),
    #url(r'^$', 'articles', name='articles'),
    url(r'^nuevo/$', new_evento, name='nuevo_eve'),
    url(r'^evento/(?P<evento_id>\d+)$', evento, name='eve_id'),
    url(r'^evento/edit/(?P<evento_id>\d+)$', edit_evento, name='eve_edit'),
    url(r'^evento/delete/(?P<evento_id>\d+)$', delete_evento, name='eve_delet'),
    url(r'^commenteve/$', commentevento, name='commenteve'),
    url(r'^ruedas/$', ruedas, name='rue'),
    url(r'^nueva/$', new_rueda, name='nueva_rue'),
    url(r'^rueda/(?P<rueda_id>\d+)$', rueda, name='rue_id'),
    url(r'^rueda/edit/(?P<rueda_id>\d+)$', edit_rueda, name='rue_edit'),
    url(r'^rueda/delete/(?P<rueda_id>\d+)$', delete_rueda, name='rue_delet'),
)
