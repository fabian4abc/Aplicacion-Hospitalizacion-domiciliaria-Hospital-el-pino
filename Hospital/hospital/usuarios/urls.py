from django.conf.urls import url,re_path
from django.urls import path, include
from usuarios import views

urlpatterns =[

path('registrar/',views.Registro_View, name="registro" ),
url(r'perfil/(?P<perfil>\d+)$',views.PerfilView,name="perfil"),
url(r'editar/(?P<usuario_id>\d+)$',views.perfil_edit, name="perfil_editar"),
url(r'tutor/datos/(?P<perfil>\d+)$',views.Tutor_view, name="tutor_form"),
url(r'paciente/datos/(?P<perfil>\d+)$',views.Paciente_view, name="paciente_form"),
url(r'personal/datos/(?P<perfil>\d+)$',views.Personal_view, name="personal_form"),
url(r'perfil/admin/',views.Perfil_admin, name="perfil_admin"),
url(r'admin/password/edit',views.contraseña_perfil_edit, name="contra_perfil_edit"),
url(r'contacto/add',views.contacto, name="contacto"),
url(r'edit/contacto',views.contacto_edit, name="contacto_edit"),


]
