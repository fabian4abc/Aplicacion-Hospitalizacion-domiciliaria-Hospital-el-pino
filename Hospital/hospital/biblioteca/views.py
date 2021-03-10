from django.shortcuts import render, redirect, get_object_or_404
from .models import Archivo, Archivo_Unico
from usuarios.models import Paciente
from django.views.generic import TemplateView ,View
from .forms import DocumentForm, DocumentFormUnico
from django.contrib import messages 
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from tutor.models import Consulta

@login_required
def biblioteca(request):
	archivo = Archivo.objects.all()    
	return render(request,'biblioteca.html',{'archivo':archivo})

@login_required
def biblioteca_unica(request,id=None):
    px=get_object_or_404(Paciente, id_tutor_id = id) 
    archivo = Archivo_Unico.objects.all()
    context={
        "px":px.id,
        "archivo":archivo,
    }
    return render(request,'biblioteca_unica.html',context)

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(biblioteca)
    else:
        form = DocumentForm()
    return render(request, 'form_archivos.html', {
        'form': form
    })

@login_required
def model_form_upload_unico(request,id=None,id_paciente=None):
    if request.method == 'POST':
        form = DocumentFormUnico(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(biblioteca_unica,id_paciente)
    else:
        form = DocumentFormUnico()
    return render(request, 'form_archivos_unico.html', {
        'form': form,'id':id
    })


@login_required
def model_form_delete(request,id=None):
    
    archivo=Archivo.objects.get(id=id)
    if request.method=='POST':
        os.remove('.'+ str(archivo.file.url))
        archivo.delete()
        return redirect(biblioteca)
    return render(request,'form_archivos_delete.html', {'archivo':archivo})
    
@login_required
def model_form_delete_unico(request,id,id_paciente):
    
    archivo=Archivo_Unico.objects.get(id=id)
    px=get_object_or_404(Paciente, id=id_paciente) 
    if request.method=='POST':
        os.remove('.'+str(archivo.file.url))
        archivo.delete()
        return redirect(biblioteca_unica,id_paciente)
    return render(request,'form_archivos_delete.html', {'archivo':archivo,'paciente':px})








