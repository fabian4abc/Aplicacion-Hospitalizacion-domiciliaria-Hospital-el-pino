from django.shortcuts import render, get_object_or_404, reverse, HttpResponse, HttpResponseRedirect, redirect
from usuarios.models import Paciente , Personal, Tutor, Perfil
from registrar.models import formulario
from tutor.models import Consulta
from visita.models import Visita
from .forms import Paciente_Form_activo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from biblioteca.models import Archivo

import numpy as np

@login_required
def logout_view(request):
    logout(request)
    return render(request,"main.html")

@login_required
def usuarios_listpa(request):
	qset = request.GET.get("buscar")
	user = Paciente.objects.filter(rut = qset)
	current_user = request.user

	if user.count() < 1:
		queryset = Paciente.objects.all()
	else:
		queryset = user	
	context = {
		"object_list": queryset,
		"actual":current_user,
	}
	return render(request,"listpa.html",context)

@login_required
def agendar_visita(request):
	qset = request.GET.get("buscar")
	user = Paciente.objects.filter(rut = qset)
	current_user = request.user

	if user.count() < 1:
		queryset = Paciente.objects.all()
	else:
		queryset = user	
	context = {
		"object_list": queryset,
		"actual":current_user,
	}
	return render(request,"lista_agendar.html",context)

@login_required
def usuarios_listen(request):
	qset = request.GET.get("buscar")
	user = Personal.objects.filter(rut = qset)
	current_user = request.user
	perfil=Perfil.objects.all()
	if user.count() < 1:
		queryset = Personal.objects.all()
	else:
		queryset = user
	context = {
		"object_list": queryset,
		"actual":current_user,	
		"perfil":perfil,
	}
	return render(request,"listen.html",context)

@login_required
def usuarios_lista(request):
	current_user = request.user
	perfil=Perfil.objects.all()
	context = {
		"object_list": perfil,
		"actual":current_user	
	}
	return render(request,"listusers.html",context)

@login_required
def usuarios_listu(request):
	qset = request.GET.get("buscar")
	user = Tutor.objects.filter(rut = qset)
	current_user = request.user
	px = Paciente.objects.all()
	if user.count() < 1:
		queryset = Tutor.objects.all()
		instance = User.objects.all()
	else:
		queryset = user
		instance = User.objects.all()
	context = {
		"object_list": queryset,
		"inst": instance,	
		"actual":current_user,
		"px":px,
	}
	return render(request,"listu.html",context)

@login_required
def consulta_lista(request):
	con = Consulta.objects.all().order_by('timestamp')
	usr = User.objects.all()
	var = 0
	context = {
		"con": con,
		"usr": usr,
		"var":var,
	}
	return render(request,"consulta_lista.html",context)

@login_required
def reingreso(request):
	qset = request.GET.get("buscar")
	user = Paciente.objects.filter(rut = qset)
	calificacion = 4
	if user.count() < 1:
		queryset = Paciente.objects.all()
	else:
		queryset = user
	context = {
		"object_list":queryset,
		"nota":calificacion,
		"rut":qset
	}
	return render(request,"reingreso.html",context)

@login_required
def reingreso_paciente(request, id=None):
	paciente=Paciente.objects.get(id=id)
	ep = paciente.episodio
	episodio = ep + 1	
	if request.method=='POST':
		paciente.episodio = episodio
		paciente.activo=1
		paciente.save()
		return redirect(usuarios_listpa)
	context = {
		"paciente":paciente,
	}
	return render(request,"confirmarreingreso.html",context)


@login_required
def dar_de_baja_paciente(request, id=None):
	paciente=Paciente.objects.get(id=id)
	episodio = paciente.episodio
	v = Visita.objects.all()
	cont = 0
	for i in v:
		if i.id_paciente == paciente.id:
			if i.status == 0:
				cont = cont + 1
	if request.method=='POST':
		paciente.activo=0
		paciente.save()
		return redirect(usuarios_listpa)
	context = {
		"paciente":paciente,
		"cont":cont,
	}
	return render(request,"dar_de_baja.html",context)


@login_required
def observaciones(request,id=None):
	px = get_object_or_404(Paciente, id=id)
	fx = formulario.objects.all()
	cont = 0
	n = 0
	for i in fx:
		if i.id_paciente == px.id:
			cont = cont + 1
			n = n + i.nota
	if n > 0:
		n = n/cont
		n = int(n)
		
	context = {
		"px":px,
		"fx":fx,
		"nota":n,
	}
	return  render(request,"observaciones.html",context)

@login_required
def obs_visita(request, id=None):
	paciente = Paciente.objects.get(id=id)
	visitas = Visita.objects.all()
	
	visitas_paciente = []

	for visita in visitas:
		if paciente.id == visita.id_paciente:
			visitas_paciente.append(visita)

	context = {
		"paciente": paciente,
		"visitas": visitas_paciente
	}
	return render(request, "observaciones_visita.html", context)