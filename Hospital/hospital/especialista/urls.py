#especialista/urls.py

from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home_especialista, name="home_e"),
    url(r'^perfil/$', views.ver_perfil_e, name="perfil_e"),
    url(r'^programadas_esp/$', views.visitas_programadas_esp, name="visitas_esp"),
    url(r'^biblioteca/$', views.biblioteca_e, name="biblioteca_e"),
    url(r'personal/edit/(?P<perfil>\d+)/(?P<id_personal>\d+)$',views.Especialista_edit, name="Especialista_edit"),
    url(r'personal/password/edit',views.contraseña_edit, name="Contra_edit"),
    ]