from django.conf.urls import url
from registrar import views

urlpatterns =[

url(r'formulario/(?P<id>\d+)$',views.formulario,name="formulario"),
url(r'formularioverdetalle/(?P<id>\d+)$',views.ver_formulario,name="ver_formulario_detalle"),
url(r'reg/(?P<id>\d+)$',views.ver_registro_admin,name="ver_registro_adm"),
url(r'reg/tutor/(?P<id>\d+)$',views.ver_registro_tutor,name="ver_registro_tutor"),
url(r'episodio/ver/(?P<id>\d+)/(?P<id_paciente>\d+)$',views.ver_episodio_numerado, name="ver_episodio_numerado"),
url(r'episodio/ver/tutor/(?P<id>\d+)/(?P<id_paciente>\d+)$',views.ver_episodio_numerado_tutor, name="ver_episodio_numerado_tutor"),
url(r'episodio/ver/esp/(?P<id>\d+)/(?P<id_paciente>\d+)$',views.ver_episodio_numerado_esp, name="ver_episodio_numerado_esp"),
url(r'episodio/historial/esp/(?P<id_visita>\d+)$',views.detalle_historial_visita_esp, name="esp_historial"),
url(r'episodio/historial/tutor/(?P<id_visita>\d+)$',views.detalle_historial_tutor, name="tutor_historial"),
]