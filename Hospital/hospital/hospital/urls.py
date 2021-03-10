from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from biblioteca import urls as biblio_urls
from dashboard import urls as dash_urls
from tutor import urls as tutor_urls
from detalle import urls as det_urls
from django.conf import settings
from django.conf.urls.static import static
from especialista import urls as especialista_urls
from equipos import urls as equipos_urls
from redireccion import urls as red
from visita import urls as agnd_visita
from registrar import urls as abc
from apis import urls
from rutas import urls


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path(r'',include('Home.urls')),
    path(r'administrador/',include('lista.urls')),
    path(r'admbiblio/',include(biblio_urls)),
    path(r'dashboard/',include(dash_urls)),
    path(r'tutor/',include(tutor_urls)),
    path(r'detalle/',include(det_urls)),
    path(r'especialista/',include(especialista_urls)),
    path(r'equipos/',include(equipos_urls)),
    path(r'red/',include(red)),
    path(r'visita/',include(agnd_visita)),
    path(r'abc/',include(abc)),
    path('', include('apis.urls')),
    path('', include('rutas.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
