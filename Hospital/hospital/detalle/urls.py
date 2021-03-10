from django.conf.urls import url,re_path
from django.urls import path, include
from detalle import views

urlpatterns =[

url(r'^paciente/(?P<id>\d+)$',views.usuario_detail, name="paciente_detalle"),
url(r'tutor/(?P<id>\d+)$',views.tutor_detail, name="tutor_detalle"),
url(r'personal/(?P<id>\d+)$',views.especialista_detail, name="especialista_detalle"),
url(r'paciente/edit/(?P<id_tutor>\d+)/(?P<id_paciente>\d+)$',views.paciente_edit, name="paciente_edit"),
url(r'tutor/edit/(?P<perfil>\d+)/(?P<id_detalle>\d+)$',views.tutor_edit, name="tutor_edit"),
url(r'personal/edit/(?P<perfil>\d+)/(?P<id_personal>\d+)$',views.especialista_edit, name="especialista_edit"),
path('<int:id>/delete',views.borrar_paciente, name='borrar_paciente'),
path('<int:id>/delete/personal',views.borrar_especialista, name='borrar_especialista'),
path('<int:id>/delete/tutor',views.borrar_tutor, name='borrar_tutor'),
url(r'consulta/edit/(?P<id>\d+)$',views.consulta_edit, name="consulta_edit"),
url(r'consulta/detalle/(?P<id>\d+)$',views.consulta_detail_adm, name="consulta_detalle_adm"),
url(r'bajapx/(?P<id>\d+)$',views.baja_paciente, name="bajapaciente"),
url(r'tipo/(?P<id>\d+)$',views.tipo_paciente, name="tipo"),

]