from django.contrib import admin 
from .models import Paciente ,Personal, Tutor, Perfil

admin.site.register(Paciente)
admin.site.register(Personal)
admin.site.register(Tutor)
admin.site.register(Perfil)
