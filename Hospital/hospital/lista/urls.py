from django.conf.urls import url,re_path
from django.urls import path, include
from lista import views

urlpatterns =[
url(r'lista/pacientes/',views.usuarios_listpa,name="listpaciente"),
url(r'lista/reingreso/',views.reingreso,name="reingreso"),
url(r'lista/personal/',views.usuarios_listen, name="listenfermero"),
url(r'lista/tutor/',views.usuarios_listu, name="listtutor"),
url(r'lista/consulta/',views.consulta_lista, name="listconsulta"),
url(r'lista/usuarios/',views.usuarios_lista, name="listusuarios"),
url(r'logout/',views.logout_view,name="logout"),
url(r'reingresopx/(?P<id>\d+)$',views.reingreso_paciente, name="reingresopaciente"),
url(r'baja/(?P<id>\d+)$',views.dar_de_baja_paciente, name="baja"),
url(r'observaciones/(?P<id>\d+)$',views.obs_visita, name="observaciones"),
url(r'agendar/', views.agendar_visita, name="agendarvisita"),

]