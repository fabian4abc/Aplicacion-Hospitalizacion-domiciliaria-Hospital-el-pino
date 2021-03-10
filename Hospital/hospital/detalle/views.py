from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect, reverse
import os
from django.contrib.auth.models import User
from django.contrib import messages
from usuarios.models import Paciente
from usuarios.models import Tutor
from usuarios.models import Personal
from usuarios.models import Perfil
from visita.models import Tiempos
from tutor.models import Consulta
from usuarios.forms import Paciente_Form , Tutor_Form , Personal_Form
from .forms import tipo
from tutor.forms import consulta_mensaje
from lista.views import usuarios_listpa, usuarios_listen, usuarios_listu 
from django.contrib.auth.decorators import login_required

@login_required
def borrar_tutor(request,id):
	paciente = get_object_or_404(Paciente, id=id)
	tutor = get_object_or_404(Tutor, id=paciente.id_tutor_id)
	user = get_object_or_404(User, id=tutor.id_perfil_id)
	if request.method == "POST":
		user.delete()
		return redirect(usuarios_listu)
	context = {	
	  "paciente":paciente,
	  "tutor":tutor,
	  "user":user,
	  "idtut":tutor.id_perfil_id,
	}
	return render(request,"delete_tutor.html",context)


@login_required
def borrar_paciente(request,id):

	paciente = get_object_or_404(Paciente, id=id)
	tutor = get_object_or_404(Tutor, id=paciente.id_tutor_id)
	user = get_object_or_404(User, id=tutor.id_perfil_id)
	if request.method == "POST":
		user.delete()
		return redirect(usuarios_listpa)
	context = {	
	  "paciente":paciente,
	  "tutor":tutor
	}
	return render(request,"delete_paciente.html",context)

@login_required
def usuario_detail(request, id=None):
	px = get_object_or_404(Paciente, id_tutor_id=id)
	tx = get_object_or_404(Tutor, id=id)
	current_user = request.user
	context = {	
		"paciente":px,
		"tutor": tx,
		"actual":current_user,
	} 
	return render(request,"detailspaciente.html",context)

@login_required
def tutor_detail(request, id=None):
	instance = get_object_or_404(User, id=id)
	detalle = get_object_or_404(Tutor, id_perfil_id=id)
	current_user = request.user
	context = {	
		"usr":instance,
		"det":detalle,
		"actual":current_user,
	} 
	return render(request,"detailstutor.html",context)

@login_required
def especialista_detail(request, id=None):
	detalle = get_object_or_404(Personal, id=id)
	instance = get_object_or_404(User, id=detalle.id_perfil_id)
	current_user = request.user
	context = {	
		"usr":instance,
		"det":detalle,
		"actual":current_user,
	} 
	return render(request,"detailspersonal.html",context)

@login_required
def paciente_edit(request,id_tutor=None,id_paciente=None):
	paciente=Paciente.objects.get(id=id_paciente)
	tutor=Tutor.objects.get(id=id_tutor)
	aux = 1
	if request.method=='GET':
		form=Paciente_Form(instance=paciente)
	else:
		form=Paciente_Form(request.POST,instance=paciente)
		if form.is_valid():
			form.save()
		return redirect(usuario_detail,id_paciente)
	return render(request,'paciente_form.html',{'form':form,'tutor':tutor,'tipo':aux,'paciente':paciente})	

@login_required
def tutor_edit(request,perfil=None,id_detalle=None):
	
	tutor=Tutor.objects.get(id=id_detalle)
	if request.method=='GET':
		form1=Tutor_Form(instance=tutor)
	else:
		form1=Tutor_Form(request.POST,instance=tutor)
		if form1.is_valid():
			form1.save()
		return redirect(tutor_detail,perfil)
	return render(request,'tutor_form.html',{'form1':form1,'perfil':perfil})

@login_required
def tipo_paciente(request,id=id):
	paciente = Paciente.objects.get(id=id)
	lista = Tiempos.objects.all()
	if request.method=='POST':
		tipo_paciente=request.POST.get('tipo')
		print(tipo_paciente)
		paciente.tipo=tipo_paciente
		paciente.save()
		return redirect(usuario_detail,id)
	context = {
		"lista":lista,
	}
	return render(request,'tipopx.html',context)	


@login_required
def especialista_edit(request,perfil=None,id_personal=None):
	personal=Personal.objects.get(id=id_personal)
	if request.method=='GET':
		form=Personal_Form(instance=personal)
	else:
		form=Personal_Form(request.POST,request.FILES, instance=personal)
		if form.is_valid():
			form.save()
		return redirect(especialista_detail,id_personal)
	return render(request,'personal_form.html',{'form':form,'perfil':perfil})

@login_required
def borrar_especialista(request,id):
	personal = get_object_or_404(Personal, id=id)
	user = get_object_or_404(User, id=personal.id_perfil_id)
	if request.method == "POST":
		os.remove("."+ str(personal.file.url))
		user.delete()
		return redirect(usuarios_listen)
	context = {	
	  "personal":personal,
	  "user":user

	}
	return render(request,"delete_personal.html",context)

@login_required
def consulta_edit(request,id=None):
	consulta=Consulta.objects.get(id=id)
	if request.method=='GET':
		form=consulta_mensaje(instance=consulta)
	else:
		form=consulta_mensaje(request.POST,instance=consulta)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('listconsulta'))
	context = {	
	  "form":form,
	  "usr":consulta,
	}	
	return render(request,'consulta_form.html',context)	

@login_required
def consulta_detail_adm(request, id=None):
	instance = get_object_or_404(Consulta, id=id)
	detalle = get_object_or_404(User, id=instance.id_usuario)
	current_user = request.user
	context = {	
		"consulta":instance,
		"usr":detalle,
	} 
	return render(request,"detailsconsulta.html",context)

@login_required
def baja_paciente(request, id=None):
	instance = get_object_or_404(Paciente, id=id)
	context = {
		"paciente":instance,
	}

	return render(request,"confirmarbaja.html",context)