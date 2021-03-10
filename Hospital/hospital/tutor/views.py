from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from biblioteca.models import Archivo, Archivo_Unico
from usuarios.models import Paciente
from usuarios.models import Tutor
from usuarios.models import Perfil
from django.contrib import messages
from django.contrib.auth.models import User
from usuarios.forms import Paciente_Form , Tutor_Form , Personal_Form
from django.views.generic import TemplateView ,View
from tutor.forms import consulta_mensaje
from tutor.models import Consulta
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

@login_required
def logout_view(request):
    logout(request)
    return render(request,"main.html")

@login_required
def home_tutor(request):
	request.session.set_expiry(0)
	current_user = request.user
	tx = instance = get_object_or_404(Tutor, id_perfil_id = current_user.id)
	px = instance = get_object_or_404(Paciente, id_tutor_id = tx.id)
	
	context = {
		"nom": current_user.first_name,
		"ape":current_user.last_name,
		"email": current_user.email,
		"id_actual":current_user.id,
		"paciente": px,
		"tutor": tx,
		"actual":current_user,
	}
	return render(request,"home_tutor.html",context)

@login_required
def ver_perfil (request):
	current_user = request.user
	tx = instance = get_object_or_404(Tutor, id_perfil_id = current_user.id)
	px = instance = get_object_or_404(Paciente, id_tutor_id = tx.id)
	tl = get_object_or_404(Perfil,id=current_user.id)
	context = {
		"nom": current_user.first_name,
		"ape":current_user.last_name,
		"email": current_user.email,
		"id_actual":current_user.id,
		"paciente": px,
		"tutor": tx,
		"actual":current_user,
		"tel":tl.tel,
		"usr":tl,
		"id_actual":current_user.id,
	}
	return render(request,"ver_perfil.html",context)

@login_required
def biblioteca_tutor(request, id=None):
	archivo = Archivo.objects.all()
	current_user =  request.user
	tx = get_object_or_404(Tutor, id_perfil_id = current_user.id)
	px = instance = get_object_or_404(Paciente, id_tutor_id = tx.id)
	archivo_unico = Archivo_Unico.objects.all()
	context = {
		"archivo":archivo,
		"archivo_unico":archivo_unico,
		"pxid":px.id,
		"paciente":px,
		"actual": current_user,
	}
	return render(request,'biblioteca_tutor.html',context)

@login_required
def Tutor_edit(request,perfil=None,id_detalle=None):
	tutor=Tutor.objects.get(id=id_detalle)
	if request.method=='GET':
		form1=Tutor_Form(instance=tutor)
	else:
		form1=Tutor_Form(request.POST,instance=tutor)
		if form1.is_valid():
			form1.save()
		return redirect(ver_perfil)
	return render(request,'tutor_f.html',{'form1':form1,'perfil':perfil,'tutor':tutor})

@login_required
def Paciente_edit(request,id_tutor=None,id_paciente=None):
	paciente = Paciente.objects.get(id=id_paciente)
	tutor = Tutor.objects.get(id=id_tutor)
	if request.method=='GET':
		form = Paciente_Form(instance=paciente)
	else:
		form = Paciente_Form(request.POST,instance=paciente)
		if form.is_valid():
			form.save()
		return redirect(ver_perfil)
	return render(request,'paciente_f.html',{'form':form,'tutor':tutor,'paciente':paciente})	

@login_required
def contacto(request):
	current_user = request.user
	tx =  get_object_or_404(Tutor, id_perfil_id = current_user.id)
	px = instance = get_object_or_404(Paciente, id_tutor_id = tx.id)
	

	form = consulta_mensaje(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(reverse('consulta_t'))

	context = {

		"form": form,
		"user": tx,
		"actual":current_user,
		"paciente":px,
	}
		
	return render(request,'Contacto.html',context)

@login_required
def ver_consultas (request):
	current_user = request.user
	tut = instance = get_object_or_404(Tutor, id_perfil_id = current_user.id)
	px = instance = get_object_or_404(Paciente, id_tutor_id = tut.id)
	tx = Tutor.objects.all()
	con = Consulta.objects.all()

	context = {

		"tutor": tx,
		"actual":current_user,
		"con":con,
		"aux":current_user.id,
		"paciente":px,


	}
	return render(request,"ver_consulta.html",context)

@login_required
def ver_respuesta (request,id=None):
	current_user = request.user
	con =  get_object_or_404(Consulta, id=id)
	tut = instance = get_object_or_404(Tutor, id_perfil_id = current_user.id)
	px = instance = get_object_or_404(Paciente, id_tutor_id = tut.id)

	context = {
		"actual":current_user,
		"con":con,
		"paciente":px,
	}
	return render(request,"ver_respuesta.html",context)

@login_required
def contraseña_edit(request):
	current_user = request.user
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect(contraseña_edit)
		else:
			messages.error(request, 'Porfavor introduzca contraseña correcta')
			return redirect(contraseña_edit)
	else:
		form = PasswordChangeForm(request.user)
		return render(request,'contra_edit.html',{'form': form, 'actual': current_user})