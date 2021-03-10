
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^listar-equipo/$', views.Listar_equipo_view, name="listar-equipo"),
	url(r'^ingresar-usuario-equipo/(?P<id>\d+)$', views.Ingreso_usuarios, name="ingresar-usuario"),
	url(r'^eliminar-equipo/(?P<id>\d+)$', views.Eliminar_equipo, name="eliminar-equipo"),

]