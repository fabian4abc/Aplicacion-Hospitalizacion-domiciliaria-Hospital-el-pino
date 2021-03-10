from django.conf.urls import url,re_path
from django.urls import path, include
from .views import visita_api, paciente_api, perfil_api, personal_api

urlpatterns = [
    path('api/visitas', visita_api),
    path('api/pacientes', paciente_api),
    path('api/perfiles', perfil_api),
    path('api/personal', personal_api),
]
