from biblioteca.models import Archivo
from visita.models import Visita
from datetime import date


#Creado con el fin de pasar elementos contadores al navbar ubidado en el archivo base.html.-

def add_variable_to_context(request):
    n_archivos= Archivo.objects.all().count() #Numero de archivos guardados en la biblioteca.
    visitas = Visita.objects.all()
    n_visitas = 0
    for visita in visitas:
        if visita.fecha == date.today():
            n_visitas += 1

    return {
        'archivos_nav':n_archivos,
        'visitas_nav':n_visitas
    }
    

    