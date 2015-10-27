__author__ = 'Ronald'
from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^registro/$', UserCreateView.as_view(), name='reg'),
	url(r'^activar/(?P<codigo>.+)/$', ActivteUserView.as_view(), name='activar_user'),
	url(r'^activo/$', UserActiveErrorView.as_view(), name='activo'),
	url(r'^activo_exito/$', UserActiveView.as_view(), name='exito_activo'),
    url(r'^error_activacion/$', ErrorActiveView.as_view(), name='error_activacion'),

]
