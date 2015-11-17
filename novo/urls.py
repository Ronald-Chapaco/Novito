from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'novo.apps.usu.views.home', name='home'),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'core/cover.html'}, name='login'),
    url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    #url(r'^signup/$', 'novo.apps.perfil.views.signup', name='signup'),
    url(r'^settings/$', 'novo.apps.usu.views.settings', name='settings'),
    url(r'^settings/picture/$', 'novo.apps.usu.views.picture', name='picture'),
    url(r'^settings/upload_picture/$', 'novo.apps.usu.views.upload_picture', name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', 'novo.apps.usu.views.save_uploaded_picture', name='save_uploaded_picture'),
    url(r'^settings/password/$', 'novo.apps.usu.views.password', name='password'),
    url(r'^network/$', 'novo.apps.usu.views.network', name='network'),
    url(r'^feeds/', include('novo.apps.feeds.urls')),
    url(r'^questions/', include('novo.apps.questions.urls')),
    url(r'^articles/', include('novo.apps.articles.urls')),
    url(r'^messages/', include('novo.apps.mensa.urls')),
    url(r'^signup/', include("novo.apps.perfil.urls")),
    url(r'^galeria/', include('novo.apps.galeria.urls')),
    url(r'^social/', include("novo.apps.evento.urls")),
    url(r'^productos/', include("novo.apps.prod.urls")),
    url(r'^notifications/$', 'novo.apps.activities.views.notifications', name='notifications'),
    url(r'^notifications/last/$', 'novo.apps.activities.views.last_notifications', name='last_notifications'),
    url(r'^notifications/check/$', 'novo.apps.activities.views.check_notifications', name='check_notifications'),
    url(r'^search/$', 'novo.apps.search.views.search', name='search'),
    url(r'^(?P<username>[^/]+)/$', 'novo.apps.usu.views.profile', name='profile'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
