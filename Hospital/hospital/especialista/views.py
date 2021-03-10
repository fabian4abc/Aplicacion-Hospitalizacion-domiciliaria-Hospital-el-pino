from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from usuarios.models import Personal , Paciente, Perfil
from visita.models import Visita

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect
from django.contrib import messages
from biblioteca.models import Archivo
from usuarios.forms import Paciente_Form , Tutor_Form , Personal_Form
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
def logout_view(request):
    logout(request)
    return render(request,"main.html")

@login_required
def home_especialista(request):
	request.session.set_expiry(0)
	current_user = request.user
	px = instance = get_object_or_404(Personal, id_perfil_id = current_user.id)
	context = {
		"actual": current_user,	
		"personal":px,
	}
	return render(request,"index_especialista.html",context)

@login_required
def ver_perfil_e (request):
	current_user = request.user
	group=Group.objects.all()
	for g in group:
		if g.name != 'Administrador' and g.name != 'Personal' and g.name != 'Tutores':
			user=User.objects.filter(groups__id=g.id)
			for u in user:
				if u.id == current_user.id:
					name=g.name
					user_group=User.objects.filter(groups__name=name)
	px = instance = get_object_or_404(Personal, id_perfil_id = current_user.id)
	tl = get_object_or_404(Perfil,id=current_user.id)
	context = {
		"actual": current_user,
		"personal":px,
		"tel":tl.tel,
		"users_group":user_group,
		"name_group":name
	}
	return render(request,"ver_perfil_e.html",context)

@login_required
def biblioteca_e(request):
	current_user = request.user
	archivo = Archivo.objects.all()
	return render(request,'biblioteca_especialista.html',{'archivo':archivo, 'actual': current_user})

@login_required
def Especialista_edit(request,perfil=None,id_personal=None):
	personal=Personal.objects.get(id=id_personal)
	if request.method=='GET':
		form=Personal_Form(instance=personal)
	else:
		form=Personal_Form(request.POST,request.FILES,instance=personal)
		if form.is_valid():
			form.save()
		return redirect(ver_perfil_e)
	return render(request,'personal_f.html',{'form':form,'perfil':perfil,'r':personal.rut})

@login_required
def contraseña_edit(request):
	current_user = request.user
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Tu password a sido cambiada exitosamente!')
			return redirect(contraseña_edit)
		else:
			messages.error(request, 'Porfavor ingrese clave correcta')
			return redirect(contraseña_edit)
	else:
		form = PasswordChangeForm(request.user)
		return render(request,'contra_especialista_edit.html',{'form': form, 'actual': current_user})
		
@login_required
def visitas_programadas_esp(request):
	current_user = request.user
	group = Group.objects.all()
	for g in group:
		if g.name != 'Administrador' and g.name != 'Personal' and g.name != 'Tutores':
			user = User.objects.filter(groups__id=g.id)
			for u in user:
				if u.id == current_user.id:
					name=g.name
					user_group = User.objects.filter(groups__name=name)
	px = instance = get_object_or_404(Personal, id_perfil_id = current_user.id)
	tl = get_object_or_404(Perfil,id=current_user.id)
	visita = Visita.objects.all()
	paciente = Paciente.objects.all()
	hoy = date.today()
	context = {
		"actual": current_user,
		"personal":px,
		"name_group":name,
		"date_list":visita,
		"hoy":hoy,
		"px":paciente
	}
	return render(request,"visitas_programadas_esp.html",context)




	